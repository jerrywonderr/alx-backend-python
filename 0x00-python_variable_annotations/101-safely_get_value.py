#!/usr/bin/python3
"""Complex annotations using TypeVar for generic typing"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[T, Any]:
    """A function that mocks the builtin get method from the dict class"""
    if key in dct:
        return dct[key]
    else:
        return default
