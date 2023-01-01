from Interface.ExpInterface import ExpInterface


class Serializer(ExpInterface):
    def __init__(self) -> None:
        super().__init__()

    def create_attrs(self, rst_cfg: dict):
        self.__dict__.update({attr: rst_cfg[attr] for attr in rst_cfg})

    def serialize(self):
        return self.__dict__
