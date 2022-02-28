"""
Module provides Node class representing prepared Lagrange polynomial
coefficients.
"""


from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange
from . import typing as _t


class Node(object):
    """
    Holds prepared Lagrange polynomial coefficients.
    """

    def __init__(self, xs: _t.NDArrayOrIterable, ys: _t.NDArrayOrIterable):
        """
        Initialize polynomial.

        Args:
            xs: X-coordinates of a set of data points.
            ys: Y-coordinates of a set of data points.
        """

        lg = lagrange(xs, ys)
        self.poly = Polynomial(lg.coef[::-1])

    def eval(self, x: _t.Number_) -> _t.Number_:
        """
        Evaluate polynomial.

        Args:
            x: Interpolation argument.

        Returns:
            Interpolation result.
        """

        return self.poly(x)
