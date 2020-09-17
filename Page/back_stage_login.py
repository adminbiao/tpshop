import logging

from Base.base import Base
from Page.pageElements import PageElements


class BackStageLogin(Base):

    def __init__(self):
        super().__init__()
        logging.info('后台管理登录页面')

    def login_page(self, name, pwd, yzm):
        """
        登录
        :param name: 输入用户名
        :param pwd: 输入密码
        :param yzm: 输入验证码
        :return:
        """
        logging.info('输入用户名:{}'.format(name))
        # 输入用户名
        self.send_ele(PageElements.username_name, name)
        logging.info('输入密码:{}'.format(pwd))
        # 输入密码
        self.send_ele(PageElements.pwd_name, pwd)
        logging.info('输入验证码:{}'.format(yzm))
        # 输入验证码
        self.send_ele(PageElements.verification_code_css, yzm)
        logging.info('点击登录按钮')
        # 点击登录
        self.click_ele(PageElements.login_css)
