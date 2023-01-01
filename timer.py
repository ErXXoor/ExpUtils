import time
import json,os
from pathlib import Path

class timer:
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

    #TODO change incrementally create new json file to base class 
    def save(self,config_path,
             exp_config,
             jc_hd,
             test_result,
             train_size=0,
             test_size=0,
             val_size=0,
             same=False)->None:
        if Path(config_path).suffix == ".json":
            if os.path.exists(config_path) and not same:
                filename = Path(config_path).stem
                filename = filename[:-1]+str(int(filename[-1])+1)
                config_path = str(Path(config_path).parent/"{}{}".format(filename,Path(config_path).suffix))
              
            with open(config_path,'w+') as f:
                config_file={}
                if same and os.path.exists(config_path):
                    config_file = json.load(f)
                
                config_file['config'] = exp_config
                config_file['timer'] = self.serialize()
                config_file['dataset'] = {"train_size":train_size,
                                          "test_size":test_size,
                                          "val_size":val_size}
                config_file['val_result'] = jc_hd
                config_file['test_result'] = test_result
                json.dump(config_file,f)
                
    def serialize(self)->dict:
        result = {}
        result['dataload_duration'] = self.dataload_dur if self.dataload_dur is not None else ""
        result['train_duration'] = self.train_dur if self.train_dur is not None else self.train_duration()
        
        return result
         