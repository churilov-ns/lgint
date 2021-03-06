"""
...
"""


from collections import defaultdict
from typing import Hashable, Optional, List, Dict
import numpy as np
from .node import Node
from . import error as _e
from . import typing as _t


class Interpolator(object):
    """
    ...
    """

    def __init__(
        self,
        xs: np.ndarray,
        ys: np.ndarray,
        *, order: Optional[int] = None,
        labels: Optional[List[Hashable]] = None,
        max_dx: Optional[_t.Number_] = None,
    ):
        """
        ...
        """

        if xs.ndim != 1 or xs.size < 2:
            raise _e.BadXShape(xs.shape)

        if ys.ndim == 1:
            ys = ys.reshape(ys.size, -1)
        if ys.ndim > 2 or ys.shape[0] != xs.size or ys.shape[1] < 1:
            raise _e.BadYShape(xs.size, ys.shape)

        if labels is None:
            labels = list(range(ys.shape[1]))
        elif len(labels) < ys.shape[1]:
            raise _e.BadLabelsCount(len(labels), ys.shape[1])

        if order is None:
            self.order = xs.size - 1
        else:
            self.order = min(order, xs.size - 1)

        self.args = xs
        self.nodes = defaultdict(list)
        self._init_nodes(ys, labels, max_dx)
        self._cache = None

    def interpolate(
        self,
        x: _t.Number_,
        targets: Optional[List[Hashable]] = None,
    ) -> Dict[Hashable, _t.Number_]:
        """
        ...
        """
        if self._cache is not None and \
                self.args[self._cache] < x <= self.args[self._cache + 1]:
            i = self._cache
        else:
            i = np.searchsorted(self.args, x)
            if i == 0 or i == self.args.size:
                raise _e.OutOfRange(x)
            i -= 1
            self._cache = i

        if targets is None:
            targets = list(self.nodes.keys())

        results = dict()
        for target in targets:
            try:
                node = self.nodes[target][i]
                if node is None:
                    raise _e.DataGap(x)
                results[target] = node.eval(x)
            except KeyError:
                raise _e.UnknownTarget(target)

        return results

    def _init_nodes(
        self,
        ys: np.ndarray,
        labels: List[Hashable],
        max_dx: Optional[_t.Number_],
    ):
        """
        ...
        """

        window = self.order + 1
        hi = window

        for i in range(self.args.size - 1):
            if hi < self.args.size and hi - i >= window // 2:
                hi += 1

            if max_dx is None:
                skip = False
            else:
                skip = self.args[i + 1] - self.args[i] > max_dx

            lo = hi - window
            for j in range(ys.shape[1]):
                if skip:
                    self.nodes[labels[j]].append(None)
                else:
                    self.nodes[labels[j]].append(Node(
                        self.args[lo:hi],
                        ys[lo:hi, j],
                    ))
