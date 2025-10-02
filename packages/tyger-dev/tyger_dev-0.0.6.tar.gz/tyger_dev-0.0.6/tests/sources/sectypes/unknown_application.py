from tyger.discipline.sectypes.types import L,unk
def baz(x: unk, y: L) -> unk:
    return y
f: unk = baz
x = f(10, True)