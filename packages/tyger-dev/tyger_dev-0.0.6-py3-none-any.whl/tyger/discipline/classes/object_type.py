class ObjectType:
    def __init__(self, name: str, bases: list[str]):
        self.name: str = name
        self.bases: list[str] = bases

        self._env: dict[str, type] = {}
    
    def __contains__(self, item: str) -> bool:
        return item in self._env

    def __getitem__(self, item: str) -> type:
        return self._env[item]

    def __setitem__(self, item: str, value: type):
        self._env[item] = value
    
    def __str__(self) -> str:
        return str(self._env)
    
    def update(self, other: dict[str, type]):
        self._env.update(other)

    @property
    def env(self) -> dict[str, type]:
        return self._env
    
    @env.setter
    def env(self, value: dict[str, type]):
        self._env = value
