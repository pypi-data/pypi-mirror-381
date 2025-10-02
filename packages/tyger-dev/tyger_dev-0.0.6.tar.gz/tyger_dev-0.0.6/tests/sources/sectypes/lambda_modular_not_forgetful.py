from typing import Callable
from tyger.discipline.sectypes.types import H,L,unk,CodType
f: Callable[[unk, unk], unk]  = lambda x,y: x + y
g: Callable[[L, H], CodType[L, L, H]] = f
h: Callable[[unk, unk], unk] = g
i: Callable[[H, H], CodType[L, L, L]] = h

x = i(1, 2)
print(x)