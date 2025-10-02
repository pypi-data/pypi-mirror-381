def foo(x: int) -> int:
    try:
        return x + 1
    except ValueError:
        return 2

y = foo(3)