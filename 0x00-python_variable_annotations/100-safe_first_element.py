#!/usr/bin/env python3
"""Duck typing"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the code with the correct duck-typed annotations:"""
    if lst:
        return lst[0]
    else:
        return None
