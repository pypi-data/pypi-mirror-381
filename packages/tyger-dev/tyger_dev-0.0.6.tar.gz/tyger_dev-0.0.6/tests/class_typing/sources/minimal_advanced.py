# Minimal advanced class patterns that definitely work with the type system

class MethodVariations:
    def __init__(self, value: int):
        self.value = value

    def greet(self, name: str = "World") -> str:
        return "Hello, " + name

    def sum_values(self, x: int, y: int) -> int:
        return self.value + x + y

    def modify_self(self, new_value: int):
        self.value = new_value
        return self

    def get_value(self) -> int:
        return self.value

class SimplePropertyClass:
    def __init__(self, value: int):
        self._value = value

    def get_value(self) -> int:
        return self._value

    def set_value(self, new_value: int) -> None:
        self._value = new_value

class MethodChaining:
    def __init__(self, value: int):
        self.value = value

    def add(self, x: int):
        self.value += x
        return self

    def multiply(self, x: int):
        self.value *= x
        return self

    def get_value(self) -> int:
        return self.value

class SimpleInheritance:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class Child(SimpleInheritance):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def get_age(self) -> int:
        return self.age
    
    def get_info(self) -> str:
        return self.name + " is " + "25" + " years old"

class MultipleInheritance:
    def __init__(self, value: int):
        self.value = value
    
    def get_value(self) -> int:
        return self.value

class Mixin:
    def mixin_method(self) -> str:
        return "mixin"

class Combined(MultipleInheritance, Mixin):
    def __init__(self, value: int, extra: str):
        self.value = value
        self.extra = extra
    
    def get_extra(self) -> str:
        return self.extra

class ClassWithClassAttrs:
    class_attr: int = 42
    name: str = "default"
    
    def __init__(self, value: int):
        self.value = value
    
    def get_both(self) -> int:
        return self.class_attr + self.value

class EmptyClass:
    pass

class ClassWithOnlyMethods:
    def method1(self) -> int:
        return 1
    
    def method2(self, x: int) -> str:
        return "hello"
    
    def method3(self, a: int, b: str) -> str:
        return "test"
