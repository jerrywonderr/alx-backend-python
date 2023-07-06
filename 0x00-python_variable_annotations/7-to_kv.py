#!/usr/bin/env python3
"""
A simple function that receives a string and
float or int and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, Union[float,int]]:
    """Receives a string and int or float and returns a tuple"""
    return (k, v**2)
