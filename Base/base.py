import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:

    def __init__(self):
        self.driver = Driver.get_tp_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元素 (属性,属性值)
        :param timeout: 搜索时间
        :param poll: 间隔时间
        :return: 返回定位对象
        """
        logging.info('操作元素:{}'.format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元素 (属性,属性值)
        :param timeout: 搜索时间
        :param poll: 间隔时间
        :return: 返回定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击操作
        :param loc: 元素 (属性,属性值)
        :param timeout: 搜索时间
        :param poll: 间隔时间
        :return:
        """
        logging.info('执行点击操作')
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        清空输入操作
        :param loc: 元素 (属性,属性值)
        :param text: 输入文本
        :param timeout: 搜索时间
        :param poll: 间隔时间
        :return:
        """
        logging.info('输入数据:{}'.format(text))
        # 定位
        input_value = self.search_ele(loc, timeout, poll)
        # 清空
        input_value.clear()
        # 输入
        input_value.send_keys(text)

    def page_exits_text(self, text):
        """
        判断页面包含某个文本
        :param text: 查找文本
        :return:
        """
        logging.info("判断页面包含文本:{}".format(text))
        text_path = (By.XPATH, "//*[contains(text(),'{}')]".format(text))
        try:
            # 定位
            self.search_ele(text_path)
            logging.info("页面存在元素:{}".format(text))
            print('\ntext{}'.format(text))
            return True
        except TimeoutException:
            logging.info("页面不存在元素:{}".format(text))
            return False

