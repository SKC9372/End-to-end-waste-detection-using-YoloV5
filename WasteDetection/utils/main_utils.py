import os.path
import sys
import yaml
import base64

from WasteDetection.exception import AppException
from WasteDetection.logger import logging

def read_yaml_file(filepath: str) -> dict:
    try:
        with open(filepath, 'r') as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e 
    
def write_yaml_file(filepath: str,content: object,replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(filepath,exist_ok=True)
        with open(filepath, 'w') as yaml_file:
            yaml.dump(content,yaml_file)
            logging.info("Wrote yaml file successfully")

    except Exception as e:
        raise AppException(e,sys) from e
    

def decode_image(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImagePath):
    with open(croppedImagePath, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string
