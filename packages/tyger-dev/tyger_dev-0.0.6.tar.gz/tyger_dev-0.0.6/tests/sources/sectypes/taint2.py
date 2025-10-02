from tyger.discipline.sectypes.types import H, L
def foo():
    x: H = 1
    if x < 2:
        return 1

z: L = foo()
print(z)