#!/usr/bin/env python3
"""A function that returns a the multiplication of floats"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by a number"""

    def multiplier_function(number: float) -> float:
        """multiplies a number by a multiplier"""
        return multiplier * number

    return multiplier_function
