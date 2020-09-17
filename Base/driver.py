from selenium import webdriver


class Driver:
    __tp_driver = None

    @classmethod
    def get_tp_driver(cls):
        """声明驱动"""
        if cls.__tp_driver is None:
            # 声明
            cls.__tp_driver = webdriver.Firefox()
            # 访问TPshop
            cls.__tp_driver.get('http://tpshop-test.itheima.net/Admin/Admin/login')
        return cls.__tp_driver

    @classmethod
    def quit_tp_driver(cls):
        """退出"""
        if cls.__tp_driver:
            cls.__tp_driver.quit()
            cls.__tp_driver = None
