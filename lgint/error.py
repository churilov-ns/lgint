"""
Specific exceptions.
"""


from typing import Tuple
from . import typing as _t


class InterpolationError(Exception):
    """
    Base error class.
    """
    pass


class BadXShape(InterpolationError):
    """
    If xs.ndim != 1 or xs.size < 2.
    """

    def __init__(self, xs_shape: Tuple):
        super().__init__(
            f'Expected xs to be 1D array of size at least 2, '
            f'got array of shape {xs_shape} instead.'
        )


class BadYShape(InterpolationError):
    """
    If ys is not 1D or 2D array, empty, or ys.shape[0] != xs.shape[0].
    """

    def __init__(self, xs_size: int, ys_shape: Tuple):
        super().__init__(
            f'Expected ys to be 1D or 2D non empty array '
            f'with ys.shape[0] == xs.shape[0] ({xs_size}), '
            f'got array of shape {ys_shape} instead.'
        )


class BadLabelsCount(InterpolationError):
    """
    If given labels count < ys.shape[1].
    """

    def __init__(self, given: int, expected: int):
        super().__init__(
            f'Labels array must be at least the same size '
            f'as ys.shape[1] ({expected}), '
            f'got array of size {given} instead.'
        )


class OutOfRangeError(InterpolationError):
    """
    If given argument is out nodes range.
    """

    def __init__(self, x: _t.Number_):
        super().__init__(f'Argument {x} is out of range.')


class DataGapError(InterpolationError):
    """
    If given argument hit in data gap.
    """

    def __init__(self, x: _t.Number_):
        super().__init__(f'Data gap at argument {x}.')
