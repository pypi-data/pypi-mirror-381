from tyger.discipline.sectypes.types import H,L,unk,CodType
def foo(x: L) -> CodType[H,H,H]:
    return x

z: unk = foo(1)
x: L = z
print(x)