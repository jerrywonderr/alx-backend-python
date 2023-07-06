#!/usr/bin/python3
"""Complex annotations using TypeVar for generic typing"""
from typing import Mapping, Any, TypeVar, NoneType, Union

T = TypeVar("T")


def safely_get_value(
        dct:Mapping, key: Any,
        default: Union[T,NoneType] = None) -> Union[T, Any]:
    """A function that mocks the builtin get method from the dict class"""
    if key in dct:
        return dct[key]
    else:
        return default
