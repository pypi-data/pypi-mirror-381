class EmptyClass:
    pass

class ClassWithOnlyAttributes:
    class_attr1: int = 10
    class_attr2: str = "hello"
    class_attr3: float = 3.14

class ClassWithOnlyMethods:
    def method1(self) -> int:
        return 1
    
    def method2(self, x: int) -> str:
        return "42"

class DeeplyNested:
    class Level1:
        class Level2:
            class Level3:
                def __init__(self, value: int):
                    self.value = value
                
                def get_value(self) -> int:
                    return self.value

class ClassWithSpecialMethods:
    def __init__(self, value: int):
        self.value = value
    
    def __str__(self) -> str:
        return "Value: 42"
    
    def __repr__(self) -> str:
        return "ClassWithSpecialMethods(42)"
    
    def __len__(self) -> int:
        return self.value
    
    def __add__(self, other: int):
        return ClassWithSpecialMethods(self.value + other)
    
    def __bool__(self) -> bool:
        return self.value != 0

class ClassWithLambda:
    def __init__(self, multiplier: int):
        self.multiplier = multiplier
    
    def get_lambda(self):
        return lambda x: x * self.multiplier
    
    def apply_lambda(self, func, value: int) -> int:
        return func(value)

class ClassWithComplexTypes:
    def __init__(self, data: dict):
        self.data = data
    
    def process_data(self):
        return "processed"
    
    def get_nested_type(self):
        return {"outer": {1: "inner"}}