from tyger.discipline.sectypes.types import H,L,unk,CodType
from typing import Callable
def baz(x: unk, y: unk) -> unk:
    return y
f: Callable[[H, L], CodType[L,L,L]] = baz
y: H = 10
z: L = True
x = f(y, z)