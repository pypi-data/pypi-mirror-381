from typing import Callable

from tyger.discipline.base.types import unk


def baz(x: unk, y: unk)-> unk:
    return x
f: Callable[[int, bool], bool] = baz
x = f(10, True)