from struct import pack, unpack
from typing import List, Any, Tuple, Iterator, Union


def _format_value(value: Any) -> str:
    if type(value) is int:
        return 'q'
    if type(value) is float:
        return 'd'
    if type(value) is bool:
        return '?'
    if type(value) is bytes:
        return 's'
    if type(value) is None:
        return 'x'
    if type(value) is tuple and len(value) == 2 and type(value[0]) is str:
        return value[0]
    raise Exception('Invalid value "%s" for network encoding' % repr(value))


def encode(*values) -> bytes:
    return pack('!' + ''.join(_format_value(value) for value in values), *values)


def _format_type(typespec: Union[type, str]) -> str:
    if type(typespec) is str:
        return typespec
    if typespec is int:
        return 'q'
    if typespec is float:
        return 'd'
    if typespec is bool:
        return '?'
    if typespec is bytes:
        return 's'
    if typespec is None:
        return 'x'


def decode(data: bytes, *types) -> tuple:
    return unpack('!' + ''.join(_format_type(typespec) for typespec in types), data)
