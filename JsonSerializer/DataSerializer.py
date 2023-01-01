from Interface.ExpInterface import ExpInterface


class DataSerializer(ExpInterface):
    def __init__(self) -> None:
        super().__init__()

    def serialize(self):
        return self.__dict__
        