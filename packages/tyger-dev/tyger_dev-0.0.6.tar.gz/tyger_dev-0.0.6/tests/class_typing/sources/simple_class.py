class Plain:
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y

    def combine(self, suffix: str) -> str:
        return self.y + suffix
