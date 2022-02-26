"""
Module provides Node class representing prepared Lagrange polynomial
coefficients.
"""


from typing import Union, Iterable
from numpy import ndarray
from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange


__all__ = [
    'Node',
]


class Node(object):
    """
    Holds prepared Lagrange polynomial coefficients.
    """

    def __init__(
        self,
        xs: Union[ndarray, Iterable],
        ys: Union[ndarray, Iterable],
    ):
        """
        Initialize polynomial.

        Args:
            xs: X-coordinates of a set of data points.
            ys: Y-coordinates of a set of data points.
        """
        lg = lagrange(xs, ys)
        self.poly = Polynomial(lg.coef[::-1])

    def eval(self, x: Union[int, float]) -> Union[int, float]:
        """
        Evaluate polynomial.

        Args:
            x: Interpolation argument.

        Returns:
            Interpolation result.
        """
        return self.poly(x)
