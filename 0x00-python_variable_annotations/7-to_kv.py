#!/usr/bin/env python3
"""A function that takes str, float or int and returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes an str, int or float and returns str which is a square of v as float"""
    return k, v**2
