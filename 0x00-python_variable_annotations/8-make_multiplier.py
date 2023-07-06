#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Simply returns a function that returns a function
    which multiplies it's input by multiplier
    """
    def multiply(n: float) -> float:
        """Mulitplies n and multiplier and returns the result"""
        return n * multiplier
    return multiply
