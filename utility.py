import pandas as pd
import sqlite3
import os
from resources.config import code_columns
from configparser import ConfigParser#, SafeConfigParser
# import sys

con = sqlite3.connect('dg_records.db', check_same_thread=False)

class Config(object):
    """
    Class for reading and writing the config file
    Author: Mike Ulloa 2020/04/16
    Sogeti Consultant
    """
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)
        self.parser = ConfigParser()
        self.config.read(config_file)

    def get_key(self, section, key):
        key_value = self.config.get(section, key)
        print(key_value)
        return(key_value)

    def get_all(self):
        config = self.config
        sections_dict = {}
        for section in config.sections():
            options = config.options(section)
            temp_dict = {}
            for option in options:
                temp_dict[option] = config.get(section, option)

            sections_dict[section] = temp_dict
        return sections_dict

    def write_key(self, section, key, value):
        parser = self.parser
        parser.read(self.config_file)

        if not parser.has_section(section):
            parser.add_section(section)

        parser.set(section, key, value)
        with open(self.config_file, 'w') as configFile:
            parser.write(configFile)


###############################################################
def update_prod_codes(df):

    for _col in code_columns:
        df[_col] = df[_col].apply(lambda x: x.zfill(3))

    return df
