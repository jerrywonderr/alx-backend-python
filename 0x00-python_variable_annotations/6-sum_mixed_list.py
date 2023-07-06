#!/usr/bin/env python3
"""
A simple function that receives a list of floats and ints
and returns their sum
"""
from typing import List, Union


def sum_mixed_list(mxd_list:List[Union[float,int]]) -> float:
    """Receives a list of floats and ints and returns their sum"""
    return sum(mxd_list)
