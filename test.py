# encoding: utf-8
# author: wm-chen
# test.py
# 2021/3/18 3:18 下午
# desc:
from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument("-user-data-dir='/Users/weimaochen/Library/Application Support/Google/Chrome/Default/'")
#option.add_extension("/Users/weimaochen/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/9.4.0_0.crx")
option.add_extension("/Users/weimaochen/clovet-test/clover-multichain-wallet/dist/chrome.crx")
driver = webdriver.Chrome(chrome_options=option, executable_path='/Users/weimaochen/PycharmProjects/uinttest/webdriver/chromedriver')
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
time.sleep(3)
#driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/button').click()