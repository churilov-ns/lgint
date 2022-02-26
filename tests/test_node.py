import pytest
import numpy as np
from lgint.node import Node


def f1(x):
    return x ** 2


def f2(x):
    return x ** 3


def f3(x):
    return 3 * x ** 2 - 2 * x


@pytest.mark.parametrize('f', [f1, f2, f3])
def test_node(f):
    xs = np.linspace(-1000.0, 1000.0, 12, endpoint=True)
    node = Node(xs, f(xs))
    for x in np.linspace(-999.0, 999.0, 100, endpoint=True):
        assert node.eval(x) == pytest.approx(f(x), rel=1.e-10)
