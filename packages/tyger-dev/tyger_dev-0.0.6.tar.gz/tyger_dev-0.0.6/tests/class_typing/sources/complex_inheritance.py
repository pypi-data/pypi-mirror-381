class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return self.name + " makes a sound"
    
    def move(self) -> str:
        return self.name + " moves"

class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool = True):
        self.name = name
        self.warm_blooded = warm_blooded
    
    def give_birth(self) -> str:
        return self.name + " gives birth to live young"

class Bird(Animal):
    def __init__(self, name: str, can_fly: bool = True):
        self.name = name
        self.can_fly = can_fly
    
    def fly(self) -> str:
        if self.can_fly:
            return self.name + " flies"
        else:
            return self.name + " cannot fly"

# Multiple inheritance
class Bat(Mammal, Bird):
    def __init__(self, name: str):
        self.name = name
        self.warm_blooded = True
        self.can_fly = True
    
    def echolocate(self) -> str:
        return self.name + " uses echolocation"

# Diamond inheritance
class FlyingMammal(Mammal):
    def __init__(self, name: str, altitude: int = 1000):
        self.name = name
        self.warm_blooded = True
        self.altitude = altitude
    
    def fly_high(self) -> str:
        return self.name + " flies at 1000 meters"

class GlidingMammal(Mammal):
    def __init__(self, name: str, glide_distance: float = 50.0):
        self.name = name
        self.warm_blooded = True
        self.glide_distance = glide_distance
    
    def glide(self) -> str:
        return self.name + " glides 50.0 meters"

class FlyingSquirrel(FlyingMammal, GlidingMammal):
    def __init__(self, name: str):
        self.name = name
        self.warm_blooded = True
        self.altitude = 500
        self.glide_distance = 75.0
    
    def special_move(self) -> str:
        return self.name + " performs a special gliding flight"

# Abstract base class like behavior
class Shape:
    def __init__(self, color: str):
        self.color = color
    
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area")
    
    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter")

class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        self.color = color
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, color: str, side: float):
        self.color = color
        self.width = side
        self.height = side
        self.side = side
    
    def diagonal(self) -> float:
        return self.side * (2 ** 0.5)
