from configparser import ConfigParser
import json


def read_config(section, key):
    try:
        config = ConfigParser()
        config.read("..\\configuration_data\\conf.ini")
        return config.get(section, key)
    except FileNotFoundError:
        pass


def remove_locator_extension(locator: str, extension: str) -> str:
    try:
        return locator.replace(extension, "")
    except None:
        pass


def load_devices_config():
    try:
        with open('../configuration_data/devices_config.json') as json_file:
            devices = json.load(json_file)
            return devices
    except FileNotFoundError:
        pass
