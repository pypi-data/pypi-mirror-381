class NamespaceContext:
    def __init__(self, env: 'Environment', namespace: str):
        self._env = env
        self._namespace = namespace

    def __enter__(self) -> 'Environment':
        self._env._namespaces.append(self._namespace)
        return self._env

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._env._namespaces.pop()


class ScopeContext:
    def __init__(self, env: 'Environment', init_scope: dict[str, type]):
        self._env = env
        self._init_scope = init_scope

    def __enter__(self) -> 'Environment':
        self._env._scopes.append(self._init_scope)
        return self._env

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._env._scopes.pop()


class Environment:
    def __init__(self, initial_envs: list[dict[str, type]] = None, namespace: list[str] = []) -> None:
        self._scopes: list[dict[str, type]] = initial_envs or [{}]
        self._namespaces: list[str] = namespace or []

    @property
    def current_scope(self) -> dict[str, type]:
        return self._scopes[-1]
    
    @property
    def namespace_env(self) -> dict[str, type] | None:
        if not self._namespaces:
            return None

        current = self.current_scope
        for namespace in self._namespaces:
            if namespace not in current:
                return None

            current = current[namespace]
        
        return current

    def __getitem__(self, key: str) -> type:
        if (namespace := self.namespace_env):
            if (var := namespace.get(key)):
                return var

        for scope in reversed(self._scopes):
            if (var := scope.get(key)):
                return var


    def __setitem__(self, key: str, value: type):
        if self.namespace_env:
            self.namespace_env[key] = value
        else:
            self.current_scope[key] = value


    def __str__(self) -> str:
        return str(self._scopes)


    def __contains__(self, key: str) -> bool:
        if self.namespace_env:
            return key in self.namespace_env
        

        for scope in reversed(self._scopes):
            if key in scope:            
                return True
        
        return False


    def __bool__(self) -> bool:
        return any(self._scopes)
    

    def update(self, updates: dict[str, type]):
        self._scopes[-1].update(updates)
    

    def in_namespace(self, namespace: str) -> 'NamespaceContext':
        return NamespaceContext(self, namespace)
    

    def in_scope(self, init_scope: dict[str, type]) -> 'ScopeContext':
        return ScopeContext(self, init_scope)


    def copy(self) -> 'Environment':
        return Environment(self._scopes.copy(), self._namespaces.copy())


    def items(self) -> list[tuple[str, type]]:
        return [(key, value) for scope in self._scopes for key, value in scope.items()]


    def keys(self) -> list[str]:
        return [item for scope in self._scopes for item in scope.keys()]


    def values(self) -> list[type]:
        return [item for scope in self._scopes for item in scope.values()]


    def pop(self, key: str) -> type:
        if self.namespace_env:
            return self.namespace_env.pop(key)

        return self.current_scope.pop(key)