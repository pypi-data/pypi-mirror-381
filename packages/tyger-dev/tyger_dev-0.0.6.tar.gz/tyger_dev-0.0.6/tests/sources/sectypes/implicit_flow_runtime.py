from tyger.discipline.sectypes.types import H,L,unk


def foo() -> L:
    y: H = 10
    x: unk = y
    if x < 20:
        return 1