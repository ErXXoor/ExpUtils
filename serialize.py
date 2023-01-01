import json
import os


class Serialize:
    @staticmethod
    def json_serialize(json_dict: dict, file_path: str):
        result = {}

        with open(file_path, 'r') as f:
            if os.path.exists(file_path):
                result = json.load(f)

            result.update(json_dict)
            json.dump(result, f)
