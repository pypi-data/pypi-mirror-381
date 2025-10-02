class A:
    def __init__(self, x: int):
        self.x = x
    
    def get_x(self) -> int:
        return self.x

class B:
    def __init__(self, s: str, n: int):
        self.s = s
        self.n = n
    
    def describe(self) -> str:
        return f"{self.s}: {self.n}"

class C:
    class_attr: int = 42
    
    def __init__(self, value: str):
        self.value = value
    
    def get_both(self) -> tuple[int, str]:
        return (self.class_attr, self.value)

class Empty:
    pass

class Parent:
    def __init__(self, p: int):
        self.p = p

class Child(Parent):
    def __init__(self, p: int, c: str):
        self.p = p
        self.c = c

# Global instantiations for testing
obj_a = A(10)
obj_b = B("hello", 42)
obj_c = C("test")
obj_empty = Empty()
obj_parent = Parent(100)
obj_child = Child(200, "child_value")
