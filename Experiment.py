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
        self.exp_config = dict()
        self.exp_module_list = list()

        if not os.path.exists(exp_path):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), exp_path)

        if pathlib.Path(exp_path).suffix not in _JSON_EXTS:
            raise FileNotFoundError("File is not {} format".format(_JSON_EXTS))

        with open(exp_path, 'r') as f:
            self.exp_config = json.load(f)

        self.init_exp_module_list()

    def init_exp_module_list(self):
        self.exp_module_list.append(DataJsonParser(self.exp_config))
        self.exp_module_list.append(ModelJsonParser(self.exp_config))

    def save(self):
        if len(self.exp_module_list) > 0:
            result = dict()
            result['exp_config'] = self.exp_config
            for module in self.exp_module_list:
                module.json_serialize(result)
            print(result)
