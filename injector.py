class Injector:
    def __init__(self):
        self.dependencies = {}

    def register(self, key, dependency):
        self.dependencies[key] = dependency

    def get_dependency(self, key):
        if key in self.dependencies:
            return self.dependencies[key]
        else:
            raise KeyError(f"Dependency '{key}' not registered.")


injector = Injector()


def inject(func):
    def wrapper(*args, **kwargs):
        func_args = func.__code__.co_varnames
        for arg_name in func_args:
            if arg_name != 'self' and arg_name in injector.dependencies:
                kwargs[arg_name] = injector.get_dependency(arg_name)
        return func(*args, **kwargs)
    return wrapper
