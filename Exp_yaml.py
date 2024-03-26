import os
from typing import Dict, List, Tuple, Type
from box import Box
import yaml


class Experiment(Box):
    def __init__(self, exp_attr) -> None:
        for key, value in exp_attr.items():
            setattr(self, key, value)
        self.apply_var([self.exp_config, self.model_config, self.data_config, self.utils_config],
                       self.var_list)

        self.exp_result = Box()
        exp_folder = self.exp_config.exp_result_folder
        if not os.path.exists(exp_folder):
            os.makedirs(exp_folder)

    def set_result(self, key: str, value: dict):
        value = Box(value)
        self.exp_result[key] = value

    def save(self, path: str):
        self.to_yaml(path)

    def apply_var(self, target_dicts: list, var_dict: Box):
        for target in target_dicts:
            for key, value in target.items():
                if isinstance(value, str):
                    for var_key, var_value in var_dict.items():
                        if "${}$".format(var_key) in value:
                            target[key] = value.replace(
                                "${}$".format(var_key), var_value)
