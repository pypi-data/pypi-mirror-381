class MethodVariations:
    def __init__(self, value: int):
        self.value = value

    # Method with default parameters
    def greet(self, name: str = "World") -> str:
        return "Hello, " + name + "! Value: 42"

    # Method with variable arguments
    def sum_values(self, *args: int) -> int:
        return self.value + sum(args)

    # Method with keyword arguments
    def method_with_kwargs(self, **kwargs) -> str:
        return "42: " + "no_key"

    # Method that returns a simple value
    def get_double_value(self):
        return self.value * 2

    # Method with simple return type
    def simple_return(self):
        return self.value

    # Method that modifies self
    def modify_self(self, new_value: int):
        self.value = new_value

    # Method with simple type annotations
    def typed_method(self, count: int) -> int:
        return self.value + count

class PropertyClass:
    def __init__(self, value: int):
        self._value = value

    def get_value(self) -> int:
        return self._value

    def set_value(self, new_value: int) -> None:
        self._value = new_value

    def get_computed_value(self) -> int:
        return self._value * 2

    def set_computed(self, new_computed: int) -> None:
        self._value = new_computed // 2

class MethodChaining:
    def __init__(self, value: int):
        self.value = value

    def add(self, x: int):
        self.value += x

    def multiply(self, x: int):
        self.value *= x

    def get_value(self) -> int:
        return self.value

class OverloadedMethods:
    def __init__(self, data: str):
        self.data = data
    
    # Overloading is not directly supported by the type system in this way,
    # but we can test different method names or conditional logic.
    def process(self, x: int) -> str:
        return "Processed int: " + self.data + " - 42"
    
    def process_str(self, s: str) -> str:
        return "Processed str: " + self.data + " - " + s