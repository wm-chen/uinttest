from selenium import webdriver
import os
from common.config_utils import local_config
from selenium.webdriver.chrome.options import Options


dri_path = os.path.dirname(__file__) + '/../' + local_config.get_driver


class Browser():
    def __init__(self,path = dri_path):
        self.driver_path = path

    def get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('lang=zh_CH.UTF-8')
        chrome_driver_path = self.driver_path + '/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        return driver




