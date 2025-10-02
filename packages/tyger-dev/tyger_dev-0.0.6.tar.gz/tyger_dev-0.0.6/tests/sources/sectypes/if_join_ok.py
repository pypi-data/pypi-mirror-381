from tyger.discipline.sectypes.types import H
def foo() -> H:
    x: H = 1
    if x < 10:
        return 1
x = foo()