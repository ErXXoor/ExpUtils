import os
from box import Box
import yaml
from jinja2 import Template


class Experiment():
    def __init__(self, exp_path) -> None:
        with open(exp_path, "r") as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        yaml_str = yaml.dump(yaml_data, default_flow_style=False)
        template = Template(yaml_str)
        yaml_str = template.render(var_list=yaml_data['var_list'])
        yaml_data = yaml.load(yaml_str, Loader=yaml.FullLoader)
        for key, value in yaml_data.items():
            if isinstance(value, dict):
                value = Box(value)
            setattr(self, key, value)

        self.exp_result = Box(yaml_data)
        exp_folder = os.path.join(
            self.var_list.output_root, self.var_list.exp_name)
        if not os.path.exists(exp_folder):
            os.makedirs(exp_folder)

    def set_result(self, key: str, value: dict):
        value = Box(value)
        self.exp_result[key] = value

    def save(self, path: str = None):
        if path is None:
            path = self.exp_config.result_file
        self.exp_result.to_yaml(path)
