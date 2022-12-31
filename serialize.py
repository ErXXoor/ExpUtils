import json
import os


class Serialize:
    @staticmethod
    def json_serialize(json_dict: dict, file_path: str):
        result = {}
        
        if os.path.exists(file_path):
            with open(file_path,'r') as f:
                result = json.load(f)
        
            