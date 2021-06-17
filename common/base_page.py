import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common import HTMLTestReportCN
from common.config_utils import local_config
from common.log_utils import logger


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        # elf.driver = webdriver.Chrome()

    # 打开网址
    def open_url(self, url):
        try:
            self.driver.get(url)
            logger.info('打开的地址为%s' % url)
        except Exception as e:
            logger.error('打开失败，原因为%s' % e)

    # 窗口最大化
    def windows_max(self):
        self.driver.maximize_window()

    # 窗口最小化
    def windows_min(self):
        self.driver.minimize_window()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 获取网页标题
    def get_title(self):
        try:
            title_text = self.driver.title
            logger.info('获取标题成功，标题为：%s' % title_text)
            return title_text
        except Exception as e:
            logger.error('获取标题失败，失败原因为:%s' % e)

    # 退出浏览器
    def quit(self):
        try:
            time.sleep(3)
            self.driver.quit()
            logger.info('退出浏览器')
        except Exception as e:
            logger.error('退出浏览器失败，原因为%s' % e)

    # 定位元素的方法
    def find_element(self, element_info):
        try:
            element_name = element_info['element_name']
            locator_type = element_info['locator_type']
            locator_value = element_info['locator_value']
            timeout = element_info['timeout']
            if locator_type == 'id':
                locator_type = By.ID
            elif locator_type == 'name':
                locator_type = By.NAME
            elif locator_type == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type == 'xpath':
                locator_type = By.XPATH
            elif locator_type == 'css':
                locator_type = By.CSS_SELECTOR
            elif locator_type == 'link':
                locator_type = By.LINK_TEXT
            # 相当于  element = driver.find_element(By.ID,value)
            element = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(locator_type, locator_value))
            logger.info('[%s]元素识别成功' % element_name)
            return element
        except Exception as e:
            logger.error('[%s]识别失败,失败原因%s' % (element_name, e.__str__()))
            self.screentshot_as_file()

    # 点击操作
    def click(self, element_info):
        try:
            element = self.find_element(element_info)
            element.click()
            logger.info('点击成功')
        except Exception as e:
            logger.error('点击失败')

    # 输入文本框操作
    def send(self, element_info, content):
        try:
            element = self.find_element(element_info)
            element.send_keys(content)
            logger.info('输入成功')
        except Exception as e:
            logger.error('输入失败')

    # 进入表单
    def switch_to_frame_by_element(self, element_info):
        try:
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)
            logger.info('成功进入[%s]表单' % element_info['element_name'])
        except Exception as e:
            logger.error('进入表单失败，失败原因为%s' % e)

    # 返回上一层表单
    def out_frame_parent(self):
        self.driver.switch_to.parent_comtent()
        logger.info('返回上一层表单')

    # 返回最外层表单
    def out_frame_default(self):
        self.driver.switch_to.default_content()
        logger.info('返回最外层表单')

    # 将页面滚动到底部
    def scroll_bottom_page(self):
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            logger.info('滚动页面到底部')
        except Exception as e:
            logger.error('滚动页面到底部失败，原因为%s' % e)

    # 报告截图
    def screentshot_as_file(self):
        report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', local_config.get_report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    # 固定等待时间
    def wait(self):
        time.sleep(3)

    # 获取元素文本
    def get_text(self, element_info):
        try:
            element = self.find_element(element_info)
            test_text = element.text
            logger.info('获取文本成功' + test_text)
            return test_text
        except Exception as e:
            logger.error('获取文本失败%s' % e)

    # 弹出框处理
    def get_alert_text(self):
        try:
            time.sleep(5)
            alert_text = self.driver.switch_to.alert.text
            logger.info('获取弹出框文本'+alert_text)
            return alert_text
        except Exception as e:
            logger.error('获取弹出框文本失败%s' % e)

    # 下拉框处理
    def get_drop_down(self, element_info, index):
        try:
            element = self.find_element(element_info)
            li = element.find_elements_by_tag_name('li')
            select_text = str(li[int(index)].text)
            li[int(index)].click()
            logger.info('选择下拉框的内容为%s' % select_text)
        except Exception as e:
            logger.error('选择下拉框失败，失败原因为%s' % e)

    # 鼠标悬浮操作
    def mouse_perform(self, element_info):
        try:
            element = self.find_element(element_info)
            ActionChains(self.driver).move_to_element(element).perform()
            logger.info("鼠标悬浮在%s" % element_info['element_name'])
        except Exception as e:
            logger.error('鼠标悬浮失败%s' % e)
