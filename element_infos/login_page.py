from common.set_driver import Browser
from common import base_page
from common.config_utils import local_config
from common.element_infos_utils import ElementInfos


class LoginPage(base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'login_element').get_element_info()
        self.username_inputbox = element_data['username_inputbox']
        self.password_inputbox = element_data['password_inputbox']
        self.login_button = element_data['login_button']

    def input_username(self, username):
        self.send(self.username_inputbox, username)

    def input_password(self, password):
        self.send(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

    def alter_text(self):
        return self.get_alert_text()


if __name__ == '__main__':
    '''    driver = Browser().get_chrome_driver()
    driver.get('http://192.168.1.15:82/zentao/user-login.html')
    driver.maximize_window()
    LoginPage(driver).input_username('admin')
    LoginPage(driver).input_password('123456')
    LoginPage(driver).click_login()'''
    element_data = ElementInfos(local_config.get_element_path, 'login_element').get_element_info()