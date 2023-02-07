import time
from easydict import EasyDict as edict

class ExpTimer:
    def __init__(self) -> None:
        self._initial_dict = edict()
        self._result_dict = edict()

    def create_timer(self,name) -> None:
        self._initial_dict[name] = time.time()
    
    def stop_timer(self,name) -> float:
        self._result_dict[name] = time.time()-self._initial_dict[name]
        return self._result_dict[name]
        
    def serialize(self,dict_name='result')->dict:
        if dict_name == 'result':
            return self._result_dict
        elif dict_name == 'initial':
            return self._initial_dict
        return {}
         