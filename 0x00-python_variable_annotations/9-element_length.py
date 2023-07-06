#!/usr/bin/env python3
"""
A more complex type annotation for a function that receives
iterables and returns a list of tuples containing each
iterable and thier length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    receives iterables and returns a list of tuples
    containing each iterable and thier length
    """
    return [(i, len(i)) for i in lst]
