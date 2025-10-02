class SimpleClass:
    def __init__(self, value: int):
        self.value = value
    
    def get_value(self) -> int:
        return self.value

class ClassWithDefaults:
    def __init__(self, x: int, y: str = "default"):
        self.x = x
        self.y = y
    
    def describe(self) -> str:
        return f"{self.x}: {self.y}"

class EmptyClass:
    pass

class ClassWithClassAttrs:
    class_attr: int = 42
    
    def __init__(self, instance_attr: str):
        self.instance_attr = instance_attr
    
    def get_both(self) -> tuple[int, str]:
        return (self.class_attr, self.instance_attr)

class Base:
    def __init__(self, base_val: int):
        self.base_val = base_val

class Child(Base):
    def __init__(self, base_val: int, child_val: str):
        self.base_val = base_val
        self.child_val = child_val
