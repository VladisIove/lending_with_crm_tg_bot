import pathlib
import os 
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
config_path = '{}/config/db.yaml'.format(cwd)
# Directory where images are saved.
DEFAULT_MEDIA_PATH = os.path.join(BASEDIR, "media/")
MEDIA_PATH = getattr(cwd, "MEDIA_PATH", None) or DEFAULT_MEDIA_PATH
# Url prefix for images.
MEDIA_URL = getattr(cwd, "MEDIA_URL", None) or "/media/"

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)