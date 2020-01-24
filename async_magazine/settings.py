import yaml
import pathlib
import os 

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'main_folder' / 'config' / 'db_confirm.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config