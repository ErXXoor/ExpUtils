from ..Interface.ExpInterface import ExpInterface


class ModelJsonParser(ExpInterface):
    def __init__(self, exp_config: dict = None) -> None:
        super().__init__()
        self.json_load(exp_config)

    def json_load(self, exp_config: dict):
        self.result_path = exp_config.get('result_path', {})
        self.model_path = exp_config.get('model_path', {})
        self.ls = exp_config.get('learning_rate', {})
        self.epoch = exp_config.get('epoch', {})
        self.batch_size = exp_config.get('batch_size', {})
        self.w_sr = exp_config.get('w_sr', {})
        self.w_tf = exp_config.get('w_tf', {})
