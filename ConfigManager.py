from easydict import EasyDict as edict
import json
import os


def cfg_from_json(config_file: str) -> edict:
    with open(config_file, 'r') as f:
        config = edict(json.loads(f.read()))
    return config


def update(config: edict, new_config: edict) -> edict:
    config.update(new_config)
    return config


def cfg_to_json(config: edict, save_path: str) -> None:
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))

    with open(save_path, 'w') as f:
        json.dump(config, f)
