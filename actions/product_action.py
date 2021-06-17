# encoding: utf-8
# author: wm-chen
# product_action.py
# 2021/3/20 3:52 下午
# desc:
import time

from element_infos.product_page import ProductPage


class ProductAction:
    def __init__(self, driver):
        self.productpage = ProductPage(driver)

    def add_products(self, name, id):
        self.productpage.click_products()
        self.productpage.send_names(name)
        self.productpage.send_ids(id)
        self.productpage.scroll_bottom_page()
        self.productpage.click_submits()
        time.sleep(3)
        return self.productpage.get_product_name()
