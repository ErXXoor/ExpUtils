import os
from pathlib import Path
from easydict import EasyDict as edict
from .ExpTimer import ExpTimer
from .ConfigManager import cfg_from_json, cfg_to_json
_JSON_EXTS = [".json"]


class Experiment:
    def __init__(self, exp_path) -> None:
        if not os.path.exists(exp_path):
            raise FileNotFoundError("File {} not found".format(exp_path))
        
        exp_config = cfg_from_json(exp_path)
        
        self._data_config = exp_config.data_config
        self._model_config = exp_config.model_config
        self._utils_config = exp_config.utils_config
        self._description = exp_config.get("description","None")
        
        self.validate_path(exp_path)
        
        self._timer_stats = ExpTimer()
        self._exp_result = edict()
        

    def save(self):
        result_path = self._model_config.exp_result_path
        self.validate_path(result_path)

        if not os.path.exists(os.path.dirname(result_path)):
            os.makedirs(os.path.dirname(result_path))
            
        self._exp_result.description=self._description
        self._exp_result.time = self._timer_stats.serialize()
        self._exp_result.model_config=self._model_config
        self._exp_result.data_config=self._data_config
            
        cfg_to_json(self._exp_result, result_path)

    def validate_path(self, file_path):
        if Path(file_path).suffix not in _JSON_EXTS:
            raise FileNotFoundError("File is not {} format".format(_JSON_EXTS))
        return True

    def update(self, new_dict: edict):
        self._exp_result.update(new_dict)
        
        
    