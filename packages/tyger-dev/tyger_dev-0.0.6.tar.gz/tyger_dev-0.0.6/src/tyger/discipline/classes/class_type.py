from .object_type import ObjectType

class ClassType:
    def __init__(self, name: str, bases: list[str]):
        self.name: str = name
        self.bases: list[str] = bases

        self._env: dict[str, type] = {}

        self._constructor_types: list[type] = []
        self._instance_type: type = None

    def __getitem__(self, item: str) -> type:
        return self._env[item]

    def __setitem__(self, item: str, value: type):
        self._env[item] = value

    def update(self, other):
        if isinstance(other, dict):
            self._env.update(other)
        elif isinstance(other, ClassType):
            self._env.update(other.env)
            
            
    def __str__(self) -> str:
        return str(self._env)

    def __contains__(self, item: str) -> bool:
        return item in self._env
    
    def get(self, item: str, default: type = None) -> type:
        return self._env.get(item, default)
    
    @property
    def env(self) -> dict[str, type]:
        return self._env
    
    @env.setter
    def env(self, value: dict[str, type]):
        self._env = value

    @property
    def constructor_types(self) -> list[type]:
        return self._constructor_types

    @constructor_types.setter
    def constructor_types(self, value: list[type]):
        self._constructor_types = value

    @property
    def instance_type(self) -> 'ObjectType':
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value: 'ObjectType'):
        self._instance_type = value