# encoding: utf-8
# author: wm-chen
# base_selenium.py
# 2021/3/6 3:04 下午
# desc:
import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.set_driver import Browser


class BaseSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.get_url

    def setUp(self):
        self.driver = Browser().get_chrome_driver()
        self.base_page = BasePage(self.driver)
        self.base_page.open_url(self.url)
        self.base_page.windows_max()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def tearDown(self):
        err = self._outcome.errors  #断言错误判断
        for test, exc_info in err:
            if exc_info:
                self.base_page.wait()
                self.base_page.screentshot_as_file()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
