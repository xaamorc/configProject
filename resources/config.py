import os
import json

class Config():
    def __init__(self) -> None:
        working_dir = os.getcwd()
        config_file = 'config.json'
        config_file_path = os.path.join(working_dir, config_file)

        with open(config_file_path, "r") as f:
            config = json.load(f)
            self.PROJECT = config['PROJECT']
            self.VERSION = config['VERSION']
            self.NAME = config['NAME']
            self.DESCRIPTION = config['DESCRIPTION']
            self.AUTHOR = config['AUTHOR']
            self.EMAIL = config['EMAIL']
            self.LICENSE = config['LICENSE']
            self.FUEL = config['FUEL']
            self.MODEL = config['MODEL']
            self.BRAND = config['BRAND']
            self.YEAR = config['YEAR']

        


