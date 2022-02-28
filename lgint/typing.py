"""
...
"""


from numbers import Number
from typing import Union, Iterable
import numpy as np


Number_ = Union[Number, np.number]
NDArrayOrIterable = Union[np.ndarray, Iterable]
