import json
import os
import pathlib
import errno
from JsonParser.DataJsonParser import DataJsonParser
from JsonParser.ModelJsonParser import ModelJsonParser
from JsonSerializer.Serializer import Serializer

_JSON_EXTS = [".json"]


class Experiment:
    def __init__(self, exp_path) -> None:
        if not os.path.exists(exp_path):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), exp_path)

        if pathlib.Path(exp_path).suffix not in _JSON_EXTS:
            raise FileNotFoundError("File is not {} format".format(_JSON_EXTS))

        with open(exp_path, 'r') as f:
            exp_config = json.load(f)

        self.init_exp_module_list(exp_config)

    def init_exp_module_list(self, exp_config: dict):
        self.data_config = DataJsonParser(exp_config)
        self.model_config = ModelJsonParser(exp_config)

    def init_rst_module_list(self):
        self.timer_stats = None
        self.dataset_stats = None
        self.metric_stats = None

    def save(self, result_path):
        result = dict()
        result['exp_config'] = self.exp_config
        for module in self.exp_module_list:
            module.json_serialize(result)
        print(result)
