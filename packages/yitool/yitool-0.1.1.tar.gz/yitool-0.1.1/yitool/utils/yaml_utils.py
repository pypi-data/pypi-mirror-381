import yaml
from os import system
from yitool.log import logger

class YamlUtils:
    @staticmethod
    def load(yaml_file: str):
        """ Loads a YAML file and returns the contents as a dictionary.
        """
        with open(yaml_file, 'r', encoding='utf-8') as stream:
            try:
                return yaml.full_load(stream)
            except yaml.YAMLError as exc:
                logger.error(f' Error loading YAML file: {yaml_file}, {exc}')
                system('exit 1')
                
    @staticmethod
    def dump(data: dict, yaml_file: str):
        """ Writes a dictionary to a YAML file.
        """
        with open(yaml_file, 'w') as stream:
            try:
                yaml.dump(data, stream, encoding='utf-8')
            except yaml.YAMLError as exc:
                logger.error(f' Error dumping YAML file: {yaml_file}, {exc}')
                system('exit 1')
