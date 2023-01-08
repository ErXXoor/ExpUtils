class ModelJsonParser():
    def __init__(self, exp_config: dict = None) -> None:
        self.json_load(exp_config)

    def json_load(self, exp_config: dict):
        self.result_path = exp_config.get('result_path', {})
        self.model_path = exp_config.get('model_path', {})
        self.learning_rate = exp_config.get('learning_rate', {})
        self.epoch = exp_config.get('epoch', {})
        self.batch_size = exp_config.get('batch_size', {})
        self.w_sr = exp_config.get('w_sr', {})
        self.w_tf = exp_config.get('w_tf', {})
        self.samples_per_epoch = exp_config.get('samples_per_epoch', {})
        self.device_number = exp_config.get('device_number', {})


class DataJsonParser():
    def __init__(self, exp_config: dict = None) -> None:
        self.json_load(exp_config)

    def json_load(self, exp_config: dict):
        self.dataset_path = exp_config.get('dataset_path', {})
        self.valset_path = exp_config.get('valset_path', {})
        self.data_augment = exp_config.get('data_augment', {})
        self.post_format = exp_config.get('post_format', {})
        self.data_preprocess = exp_config.get(
            'data_preprocess', {})
        self.input_img_size = exp_config.get('input_img_size', {})
        self.crop_size = exp_config.get('crop_size', {})
        # self.data_dict["guide_img_size"] = [i // 2 for i in self.crop_size]
