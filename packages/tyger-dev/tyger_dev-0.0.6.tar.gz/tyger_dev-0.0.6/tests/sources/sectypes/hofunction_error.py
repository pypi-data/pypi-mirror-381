from tyger.discipline.sectypes.types import H,L,unk,CodType
from typing import Callable

def baz(x: unk, y: L) -> unk:
    return y
f: Callable[[H, unk], CodType[L,L,L]] = baz
print(f)
y: H = 10
z: H = True
x = f(y, z)