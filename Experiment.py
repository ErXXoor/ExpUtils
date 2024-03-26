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
        self.validate_path(exp_path)

        exp_config = cfg_from_json(exp_path)

        self._exp_config = exp_config.get("exp_config", None)
        self._data_config = exp_config.get("data_config", None)
        self._model_config = exp_config.get("model_config", None)
        self._train_config = exp_config.get("train_config", None)
        self._utils_config = exp_config.get("utils_config", None)
        self._description = exp_config.get("description", None)

        var_list = exp_config.get("var_list", None)
        self.apply_var([self._exp_config, self._model_config, self._data_config,
                       self._utils_config], var_list)

        exp_folder = self._exp_config.exp_folder
        if not os.path.exists(exp_folder):
            os.makedirs(exp_folder)

        self._timer_stats = ExpTimer()
        self._exp_result = edict()

    def save(self):
        result_path = self._model_config.exp_result_path
        self.validate_path(result_path)

        self._exp_result.description = self._description if self._description else "No description"

        self._exp_result.time = self._timer_stats.serialize()

        self._exp_result.model_config = self._model_config if self._model_config else "No model config"

        self._exp_result.train_config = self._train_config if self._train_config else "No train config"

        self._exp_result.data_config = self._data_config if self._data_config else "No data config"

        cfg_to_json(self._exp_result, result_path)

    def validate_path(self, file_path):
        if Path(file_path).suffix not in _JSON_EXTS:
            raise FileNotFoundError("File is not {} format".format(_JSON_EXTS))
        return True

    def update(self, new_dict: edict):
        self._exp_result.update(new_dict)

    def apply_var(self, target_dicts: list, var_dict: edict):
        for target in target_dicts:
            for key, value in target.items():
                if isinstance(value, str):
                    for var_key, var_value in var_dict.items():
                        if "${}$".format(var_key) in value:
                            value = value.replace(
                                "${}$".format(var_key), var_value)
                            target[key] = value
