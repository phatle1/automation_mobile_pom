from configparser import ConfigParser
from pathlib import Path

parent_path = Path(__file__).resolve().parents[1]
db_conf = f'{parent_path}/data_access_object/database.ini'


def load_db_config(section):
    parser = ConfigParser()
    parser.read(db_conf)
    config_db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, db_conf))
    return config_db


if __name__ == '__main__':
    config = load_db_config
    print(config)
