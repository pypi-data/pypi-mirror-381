from tyger.discipline.sectypes.types import H, L, unk
def foo(x: L) -> H:
    return x

z: unk = foo(1)
x: L = z
print(x)