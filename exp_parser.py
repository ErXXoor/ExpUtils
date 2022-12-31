import json
import os
import pathlib

_JSON_EXTS = {".json"}

class ExpParser:
    def __init__(self,exp_path=None)->None:
        self.model_dict = dict()
        self.data_dict = dict()
                
        if exp_path!=None:
            with open(exp_path,'r') as f:
                if pathlib.Path(exp_path).suffix in _JSON_EXTS:
                    exp_config = json.load(f)
                    self.model_dict = self.parse_model_dict(exp_config)
                    self.data_dict = self.parse_data_dict(exp_config)
                    
    def parse_model_dict(self,exp_config:dict):
        self.model_dict["result_path"] = exp_config.get('result_path',{})
        self.model_dict["model_path"] = exp_config.get('model_path',{})
        self.model_dict["ls"] = exp_config.get('learning_rate',{})
        self.model_dict["epoch"] = exp_config.get('epoch',{})
        self.model_dict['batch_size'] = exp_config.get('batch_size',{})
        self.model_dict["w_sr"] = exp_config.get('w_sr',{})
        self.model_dict['w_tf'] = exp_config.get('w_tf',{})
        
    def parse_data_dict(self,exp_config:dict):
        self.data_dict["dataset_path"] = exp_config.get('dataset_path',{})
        self.data_dict['data_augment'] = exp_config.get('data_augment',{})
        self.data_dict["post_format"] = exp_config.get('post_format',{})
        self.data_dict["data_preprocess"] = exp_config.get('data_preprocess', {})
        self.data_dict["img_size"] = exp_config.get('input_img_size',{})
        self.data_dict["crop_size"] = exp_config.get('crop_size',{})
        self.data_dict["guide_img_size"] = [i // 2 for i in self.crop_size]
        
    