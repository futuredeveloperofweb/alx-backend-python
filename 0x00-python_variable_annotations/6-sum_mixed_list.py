#!/usr/bin/env python3
"""A function that takes floats as argument and returns the sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum as a float"""
    return sum(mxd_lst)
