import json
from configparser import ConfigParser
from pathlib import Path

parent_path = Path(__file__).resolve().parents[1]
conf = f'{parent_path}/configuration_data/conf.ini'


def read_config(section, key):
    try:
        config = ConfigParser()
        config.read(conf)
        return config.get(section, key)
    except FileNotFoundError:
        pass


def remove_locator_extension(locator: str, extension: str) -> str:
    try:
        return locator.replace(extension, "")
    except None:
        pass


def load_devices_config(file_path):
    try:
        with open(file_path) as json_file:
            devices = json.load(json_file)
            return devices
    except FileNotFoundError:
        pass
