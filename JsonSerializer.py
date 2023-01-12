
class Dataset_stats():
    def __init__(self) -> None:
        self.train_size = 0
        self.test_size = 0
        self.val_size = 0


class Metric_stats():
    def __init__(self) -> None:
        self.ce = 0.0
        self.dice = 0.0
        self.jc = 0.0
        self.hd = 0.0
