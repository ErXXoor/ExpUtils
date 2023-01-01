from Interface.ExpInterface import ExpInterface


class DataJsonParser(ExpInterface):
    def __init__(self, exp_config: dict = None) -> None:
        super().__init__()
        self.json_load(exp_config)

    def json_load(self, exp_config: dict):
        self.dataset_path = exp_config.get('dataset_path', {})
        self.data_augment = exp_config.get('data_augment', {})
        self.post_format = exp_config.get('post_format', {})
        self.data_preprocess = exp_config.get(
            'data_preprocess', {})
        self.input_img_size = exp_config.get('input_img_size', {})
        self.crop_size = exp_config.get('crop_size', {})
        # self.data_dict["guide_img_size"] = [i // 2 for i in self.crop_size]
