import torch
import ConfigManager as cfg


class Data_loader(torch.utils.data.Dataset):
    def __init__(self, config_path):
        self._config = cfg.cfg_from_json(config_path)["data_config"]
