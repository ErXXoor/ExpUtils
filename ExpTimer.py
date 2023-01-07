import time

class ExpTimer:
    def __init__(self) -> None:
        self.dataload_start = None
        self.train_start = None
        self.epoch_start = None
        self.train_dur = None
        self.dataload_dur = None
        self.timer_start = time.time()

    def dataload_init(self) -> None:
        self.data_loading_start = time.time()

    def train_init(self) -> None:
        self.train_start = time.time()

    def epoch_init(self) -> None:
        self.epoch_start = time.time()      

    def epoch_duration(self) -> float:
        duration = float()
        if self.epoch_start is not None:
            duration = time.time()-self.epoch_start
        elif self.train_start is not None:
            duration = time.time()-self.train_start
        else:
            duration = time.time()-self.timer_start

        self.epoch_start = time.time()
        return duration

    def dataload_duration(self) -> float:
        self.dataload_dur = time.time()-self.dataload_start if self.dataload_start is not None else time.time()-self.timer_start

        return self.dataload_dur

    def train_duration(self) -> float:
        self.train_dur = time.time()-self.timer_start if self.train_start is None else time.time()-self.train_start
        
        return self.train_dur
                
    def serialize(self)->dict:
        result = {}
        result['dataload_duration'] = self.dataload_dur if self.dataload_dur is not None else ""
        result['train_duration'] = self.train_dur if self.train_dur is not None else self.train_duration()
        
        return result
         