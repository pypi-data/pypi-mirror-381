from tyger.discipline.sectypes.types import H,L,unk,CodType
from typing import Callable
f: Callable[[L, unk], CodType[L, L, L]] = lambda x,y: x + y
y: H = True
x = f(1, y)