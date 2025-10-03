import itertools
import operator
import re
import urllib.error
import urllib.parse
import urllib.request
from base64 import b64decode, b64encode
from collections.abc import MutableMapping
from importlib import import_module
from typing import Any

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from django.conf import settings
from django.db.models import Q
from django.urls import reverse

from dynforms.fields import value_to_list

FIELD_SEPARATOR = '__'


def _toInt(val, default=None):
    try:
        return int(val)
    except ValueError:
        return default


def get_module(app, modname, verbose, failfast):
    """
    Internal function to load a module from a single app.
    """
    module_name = f'{app}.{modname}'
    try:
        module = import_module(module_name)
    except ImportError as e:
        if failfast:
            raise e
        elif verbose:
            print("Could not load {!r} from {!r}: {}".format(modname, app, e))
        return None
    if verbose:
        print("Loaded {!r} from {!r}".format(modname, app))
    return module


def load(modname, verbose=False, failfast=False):
    """
    Loads all modules with name 'modname' from all installed apps.

    If verbose is True, debug information will be printed to stdout.

    If failfast is True, import errors will not be suppressed.
    """
    for app in settings.INSTALLED_APPS:
        get_module(app, modname, verbose, failfast)


def dict_list(d):
    """
    Recursively convert a dictionary with integer-like string keys into a list,
    sorting by the integer value of the keys. If the dictionary does not have
    all integer-like keys, recursively process its values.

    Args:
        d (dict or any): The dictionary (or value) to process.

    Returns:
        list, dict, or any: A list if all keys are integer-like, otherwise a dict,
        or the value itself if not a dict.
    """
    if not isinstance(d, dict):
        return d

    # Try to convert all keys to integers (or None if not possible)
    int_keys = {k: _toInt(k) for k in d.keys()}

    # If all keys are integers, return a list sorted by key
    if all(isinstance(v, int) for v in int_keys.values()):
        sorted_items = sorted(
            ((int_keys[k], dict_list(d[k])) for k in d.keys()),
            key=lambda pair: pair[0]
        )
        return [item for _, item in sorted_items]
    else:
        # Otherwise, recursively process values
        return {k: dict_list(v) for k, v in d.items()}


class DotExpandedDict(dict):
    """
    A special dictionary constructor that takes a dictionary in which the keys
    may contain dots to specify inner dictionaries. It's confusing, but this
    example should make sense.

    >>> d = DotExpandedDict({'person.1.firstname': ['Simon'], \
    'person.1.lastname': ['Willison'], \
    'person.2.firstname': ['Adrian'], \
    'person.2.lastname': ['Holovaty']})
    >>> d
    {'person': {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}}
    >>> d['person']
    {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}
    >>> d['person']['1']
    {'lastname': ['Willison'], 'firstname': ['Simon']}

    # Gotcha: Results are unpredictable if the dots are "uneven":
    >>> DotExpandedDict({'c.1': 2, 'c.2': 3, 'c': 1})
    {'c': 1}
    """

    def __init__(self, key_to_list_mapping):
        super().__init__()
        for k, v in list(key_to_list_mapping.items()):
            current = self
            bits = re.split(rf'\.|{FIELD_SEPARATOR}', k)
            for bit in bits[:-1]:
                current = current.setdefault(bit, {})
            # Now assign value to current position
            try:
                current[bits[-1]] = v
            except TypeError:  # Special-case if current isn't a dict.
                current = {bits[-1]: v}

    def with_lists(self):
        return dict_list(self)


def build_Q(rules):
    """
    Build and return a Q object for a list of rule dictionaries
    """
    q_list = []
    for rule in rules:
        nm = rule['field'].replace('-', '_')
        q_list.append(Q(**{
            f"{rule['field']}__{rule['operator']}": rule['value']
        }))
    qRule = q_list.pop(0)
    for item in q_list:
        qRule |= item

    return qRule


def _get_nested(obj, fields, required=True):
    if required:
        a = obj[fields.pop(0)]
    else:
        a = obj.get(fields.pop(0), None)
    if not len(fields):
        return a
    else:
        return _get_nested(a, fields)


def get_nested(obj, field_name, required=True):
    """
    A dictionary implementation which supports extended django field names syntax
    such as employee__person__last_name.
    """
    if field_name == '*':
        return obj  # interpret special character '*' as pointing to self
    else:
        return _get_nested(obj, field_name.split('__'), required)


def get_nested_list(obj, field_names, required=True):
    """
    Get for a list of extended fields.
    """
    return [get_nested(obj, field_name, required) for field_name in field_names]


def flatten_dict(data: dict, parent: str = '') -> dict:
    """
    Flatten a nested dictionary by replacing the keys with a dots or double-underscore
    :param data: Dictionary to flatten
    :param parent: optional parent key to prepend to the keys
    :return: flattened dictionary
    """
    items = {}
    for key, value in data.items():
        key = key.replace('-', '_')
        new_key = f"{parent}{FIELD_SEPARATOR}{key}" if parent else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key))
        else:
            items[new_key] = value
    return items


def expand_dict(d: dict) -> dict:
    """
    Expand a flattened dictionary into a nested dictionary. Key levels are separated by dots or double underscores
    :param d: Dictionary to expand
    :return: nested dictionary
    """
    items = DotExpandedDict(d)
    return dict_list(items)


FIELD_OPERATOR_CHOICES = [
    ("lt", "Less than"),
    ("gt", "Greater than"),
    ("lte", "Equal or Less than"),
    ("gte", "Equal or Greater than"),
    ("exact", "Exactly"),
    ("iexact", "Exactly (Any case)"),
    ("neq", "Not Equal to"),
    ("in", "Contained In"),
    ("contains", "Contains"),
    ("nin", "Not Contained In"),
    ("startswith", "Starts With"),
    ("endswith", "Ends With"),
    ("istartswith", "Starts With (Any case)"),
    ("iendswith", "Ends With (Any case)"),
    ("isnull", "Is Empty"),
    ("notnull", "Is Not Empty"),
]

FIELD_OPERATORS = {
    "lt": operator.lt,
    "lte": operator.le,
    "exact": operator.eq,
    "iexact": lambda x, y: operator.eq(x.lower(), y.lower()),
    "neq": operator.ne,
    "gte": operator.ge,
    "eq": operator.eq,
    "gt": operator.gt,
    "in": lambda x, y: operator.contains(y, x),
    "contains": operator.contains,
    "range": lambda x, y: y[0] <= x <= y[1],
    "startswith": lambda x, y: x.startswith(y),
    "istartswith": lambda x, y: y.lower().startswith(x.lower()),
    "endswith": lambda x, y: x.startswith(y),
    "iendswith": lambda x, y: x.lower().startswith(y.lower()),
    "nin": lambda x, y: not operator.contains(x, y),
    'isnull': lambda x, y: False if x else True,
    'notnull': lambda x, y: True if x else False,
}


class Queryable(object):
    """Converts a dictionary into an object which can be queried using django 
    Q objects"""

    def __init__(self, data):
        self.data = flatten_dict(data)

    def matches(self, q):
        if isinstance(q, tuple):
            key, value = q
            parts = key.split(FIELD_SEPARATOR)
            if parts[-1] in list(FIELD_OPERATORS.keys()):
                field_name = FIELD_SEPARATOR.join(parts[:-1])
                field_operator = FIELD_OPERATORS[parts[-1]]
                # operator_name = parts[-1]
            else:
                field_name = FIELD_SEPARATOR.join(parts)
                field_operator = FIELD_OPERATORS['exact']
                # operator_name = 'exact'
            if not field_name in self.data:
                return False
            else:
                field_value = self.data[field_name]
            return field_operator(field_value, value)
        elif isinstance(q, Q):
            if q.connector == 'OR':
                return any(self.matches(c) for c in q.children)
            elif q.connector == 'AND':
                return all(self.matches(c) for c in q.children)
        elif isinstance(q, bool):
            return q
        else:
            return False


def get_process_reqs(wf_spec):
    def _get(v):
        return isinstance(v, dict) and list(v.values()) or [v]

    var_lists = itertools.chain.from_iterable([t.get('uses', []) for t in list(wf_spec['tasks'].values())])
    new_reqs = set(itertools.chain.from_iterable(_get(e) for e in var_lists))
    return list(new_reqs)


def get_task_reqs(name, wf_reqs):
    reqs = []
    for itm in wf_reqs:
        parts = itm.split(FIELD_SEPARATOR)
        if name == parts[0]:
            reqs.append(FIELD_SEPARATOR.join(parts[1:]))
    return reqs


def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.parse.urlencode(get)
    return url


class Crypt:
    enc_dec_method = 'utf-8'
    key = getattr(settings, "USO_THROTTLE_KEY", get_random_bytes(16))

    @classmethod
    def encrypt(cls, str_to_enc):
        try:
            aes_obj = AES.new(cls.key, AES.MODE_CFB)
            hx_enc = aes_obj.encrypt(str_to_enc.encode('utf8'))
            msg = b64encode(hx_enc).decode(cls.enc_dec_method)
            salt = b64encode(aes_obj.iv).decode(cls.enc_dec_method)
            return f"{salt}|{msg}"
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

    @classmethod
    def decrypt(cls, enc_msg):
        try:
            salt_enc, enc_str = enc_msg.split('|')
            salt = b64decode(salt_enc.encode(cls.enc_dec_method))
            aes_obj = AES.new(cls.key, AES.MODE_CFB, salt)
            str_tmp = b64decode(enc_str.encode(cls.enc_dec_method))
            str_dec = aes_obj.decrypt(str_tmp)
            msg = str_dec.decode(cls.enc_dec_method)
            return msg
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)


class FormFieldManager:
    def __init__(self, name=None, field_type=None, label='', instructions='', options=None, index=0, **attrs):
        from .fields import FieldType
        self.name = name
        self.index = index
        self.field_type = field_type
        self.type = FieldType.get_type(field_type)
        self.label = label
        self.instructions = instructions
        self.attrs = attrs
        self.options = options or []

    def specs(self, repeatable=False, index=0):
        return {
            'name': self.name if not repeatable else f"{self.name}{FIELD_SEPARATOR}{index}",
            'index': self.index,
            'field_type': self.field_type,
            'label': self.label,
            'instructions': self.instructions,
            'type': self.type,
            'manager': self,
            'options': self.options,
            **self.attrs,
        }

    def show_sublabels(self):
        return 'labels' in self.options or 'floating' in self.options

    def width_styles(self):
        width = self.attrs.get('width', 'full')
        return {
            'full': 'col-12',
            'half': 'col-6',
            'third': 'col-4',
            'quarter': 'col-3',
            'two_thirds': 'col-8',
            'three_quarters': 'col-9',
            'auto': 'col-auto',
        }.get(width, 'col-12')

    def get_max_repeat(self):
        """
        Returns the maximum number of times this field can be repeated.
        If 'repeat' is not in options, returns 1.
        """
        if not self.is_repeatable() or self.attrs.get('max_repeat', None) is None:
            return 0
        return self.attrs.get('max_repeat', 0)

    def hide_styles(self):
        return 'df-hide' if 'hide' in self.options else ''

    def extra_styles(self):
        return self.attrs.get("tags", "")

    def is_required(self) -> bool:
        return 'required' in self.options

    def is_inline(self) -> bool:
        return 'inline' in self.options

    def is_multi_valued(self) -> bool:
        return 'multiple' in self.options or self.type.is_multi_valued()

    def is_repeatable(self) -> bool:
        return 'repeat' in self.options

    def get_choices(self):
        return self.attrs.get('choices', [])

    def get_options(self):
        return self.options

    def set_attr(self, name, value):
        self.attrs[name] = value

    def missing_subfields(self, data) -> list[str]:
        """
        Validate the subfields of the field type.
        :param data: The data to validate.
        :return: A list of invalid subfield names.
        """
        if not self.type:
            return []

        if (self.is_multi_valued() or self.is_repeatable()) and isinstance(data, list):
            validity = {}
            for row in data:
                single_validity = self.type.check_entry(row)
                for key, value in single_validity.items():
                    validity[key] = value if key not in validity else min(validity[key], value)
        elif isinstance(data, dict):
            validity = self.type.check_entry(data)
        else:
            validity = {}
        return [k for k, v in validity.items() if not v]

    def get_data(self, context):
        default = self.attrs.get('default', None)
        form = context.get('form')

        if not form or self.type is None:
            return default

        if form.is_bound:
            data = form.cleaned_data.get('details', {})
            value = data.get(self.name)
            if value is not None:
                return self.type.compress(value)

        if getattr(form, 'instance', None) and hasattr(form.instance, 'get_field_value') and form.instance.pk:
            value = form.instance.get_field_value(self.name)
            if value is not None:
                return self.type.compress(value)

        value = form.initial.get(self.name, default)
        return '' if value is None else self.type.compress(value)

    def normalize_data(self, data, multi: bool = False) -> Any:
        """
        Normalize the data for this field. make sure lists are present when needed and not
        present if not needed.
        :param data: The data to normalize.
        :param multi: If True, the data is expected to be multivalued.
        """

        if multi and isinstance(data, list):
            data = [self.normalize_data(item) for item in data if item is not None]
        elif multi:
            data = [self.normalize_data(data)]
        elif isinstance(data, dict):
            # clean subfields
            new_data = {}
            for key, value in data.items():
                value = self.normalize_data(value, multi=self.type.is_multi_valued(key))
                if value in [None, '', [], {}]:
                    continue
                clean_method = getattr(self.type, f'clean_{key}', None)
                if callable(clean_method):
                    new_data[key] = clean_method(value)
                else:
                    new_data[key] = value

            data = {k: v for k, v in new_data.items() if v not in [None, '', [], {}]}
        elif isinstance(data, list) and len(data) == 1:
            data = self.normalize_data(data[0])
        elif isinstance(data, str):
            data = data.strip()

        return data

    def clean(self, data):
        """
        Clean the data for this field. This method should be overridden by subclasses
        to implement specific cleaning logic.
        """
        multi = self.is_multi_valued() or self.is_repeatable()
        data = self.normalize_data(data, multi=multi)
        return self.type.clean(data)


class FormPageManager:
    """
    A manager for a page in a form, which contains multiple fields managers
    """
    def __init__(self, name='', fields=None, number=1):
        self.number = number
        self.name = name
        fields = fields or []
        self.fields = [
            FormFieldManager(**field, index=i) for i, field in enumerate(fields) if isinstance(field, dict)
        ]
        self.field_indices = {field.name: i for i, field in enumerate(self.fields)}

    def get_field(self, name):
        """
        Get a field by its name.
        :param name: The name of the field to retrieve.
        :return: The FormField object if found, otherwise None.
        """
        return self.fields[self.field_indices[name]] if name in self.field_indices else None



