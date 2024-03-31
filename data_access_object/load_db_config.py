from configparser import ConfigParser
from pathlib import Path

parent_path = Path(__file__).resolve().parents[1]
db_conf = f'{parent_path}/data_access_object/database.ini'


def load_config(filename=db_conf, section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    config_db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config_db


if __name__ == '__main__':
    config = load_config()
    print(config)
