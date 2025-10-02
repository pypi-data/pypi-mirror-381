from tyger.discipline.sectypes.types import L,CodType
from typing import Callable
f: Callable[[L, L], CodType[L, L, L]] = lambda x,y: x + y
x = f(1,2)