# encoding: utf-8
# author: wm-chen
# my_page.py
# 2021/3/10 4:43 下午
# desc:

from common import base_page
from common.config_utils import local_config
from common.element_infos_utils import ElementInfos


class MyPage(base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'login_element').get_element_info()
        self.username_inputbox = element_data['username_inputbox']
        self.password_inputbox = element_data['password_inputbox']
        self.login_button = element_data['login_button']