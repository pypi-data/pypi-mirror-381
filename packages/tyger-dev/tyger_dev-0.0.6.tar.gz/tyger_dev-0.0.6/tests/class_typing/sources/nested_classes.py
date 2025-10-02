class Outer:
    outer_attr: int = 10

    def __init__(self, name: str):
        self.name = name

    class Inner:
        def __init__(self, value: str):
            self.value = value

        def get_value(self) -> str:
            return self.value

        def set_value(self, new_value: str):
            self.value = new_value

    def get_outer_name(self) -> str:
        return self.name