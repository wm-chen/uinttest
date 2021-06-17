# encoding: utf-8
# author: wm-chen
# product_page.py
# 2021/3/10 4:43 下午
# desc: 产品页面

from common import base_page
from common.element_infos_utils import ElementInfos
from common.config_utils import local_config


class ProductPage(base_page.BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'product_element').get_element_info()
        self.add_product = element_data['add_product']
        self.send_name = element_data['send_name']
        self.send_id= element_data['send_id']
        self.click_submit = element_data['click_submit']
        self.product_name=element_data['product_name']

    def click_products(self):
        self.click(self.add_product)

    def send_names(self,name):
        self.send(self.send_name, name)

    def send_ids(self,id):
        self.send(self.send_id, id)

    def click_submits(self):
        self.click(self.click_submit)

    def get_product_name(self):
        return self.get_text(self.product_name)











