import os
import configparser

condig_path = os.path.dirname(__file__) + '/../conf/config.ini'


class ConfigUtils(object):
    def __init__(self,path=condig_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding='utf-8')

    @property
    def get_url(self):
       value = self.cfg.get('default', 'url')
       return value

    @property
    def get_driver(self):
        value = self.cfg.get('default', 'driver')
        return value

    @property
    def get_username(self):
        value = self.cfg.get('default', 'username')
        return value

    @property
    def get_password(self):
        value = self.cfg.get('default', 'password')
        return value

    @property
    def get_case_path(self):
        value = self.cfg.get('default', 'case_path')
        return value

    @property
    def get_test_case_path(self):
        value = self.cfg.get('default', 'test_case_path')
        return value

    @property
    def get_report_path(self):
        value = self.cfg.get('default', 'report_path')
        return value

    @property
    def get_element_path(self):
        value = self.cfg.get('default', 'element_path')
        return value

local_config = ConfigUtils()

