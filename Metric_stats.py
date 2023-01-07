from .Serializer import Serializer


class Metric_stats(Serializer):
    def __init__(self) -> None:
        super().__init__()
        self.test = Serializer()
        self.test.ce = float
        self.test.dice = float
        self.test.jc = float
        self.test.hd = float

        self.val = Serializer()
        self.test.ce = float
        self.val.dice = float
        self.val.jc = float
        self.val.hd = float

    def serialize(self):
        return {"val_result": self.test.serialize(), "test_result": self.val.serialize()}
