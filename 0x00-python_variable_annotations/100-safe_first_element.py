#!/usr/bin/env python3
"""More complex annotations for sporadic functions"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element in an iterable else None"""
    if lst:
        return lst[0]
    else:
        return None
