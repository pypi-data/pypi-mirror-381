def create_local_class():
    class LocalClass:
        def __init__(self, value: int):
            self.value = value
        
        def get_value(self) -> int:
            return self.value
    
    return LocalClass

def create_local_class_with_methods():
    class LocalClassWithMethods:
        def __init__(self, name: str):
            self.name = name
        
        def greet(self) -> str:
            return "Hello, " + self.name
        
        def get_name(self) -> str:
            return self.name
    
    return LocalClassWithMethods

# Global class for comparison
class GlobalClass:
    def __init__(self, data: str):
        self.data = data
    
    def process(self) -> str:
        return "Processed: " + self.data
