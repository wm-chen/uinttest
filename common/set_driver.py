import time

from selenium import webdriver
import os
from common.config_utils import local_config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


dri_path = os.path.dirname(__file__) + '/../' + local_config.get_driver


class Browser(object):

    def __init__(self, path=dri_path):
        self.driver_path = path

    def get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('lang=zh_CH.UTF-8')
        chrome_driver_path = self.driver_path + '/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        return driver


if __name__ == '__main__':
    driver = Browser().get_chrome_driver()
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
    driver.maximize_window()
    '''    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="J_6977698868"]/div/div/div[2]/div[2]/div[1]')).perform()
    time.sleep(3)
    driver.find_element_by_link_text('裙子').click()'''





