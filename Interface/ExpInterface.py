
class ExpInterface:
    def __init__(self) -> None:
        pass

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
