import logging

import pytest
from Base.data import Data
from Base.driver import Driver
from Base.page import Page


def mis_login_data():
    # 空列表
    mis_login_list = []
    # 读数据
    login_data = Data.get_json_data("login_data.json")
    # 追加数据
    for i in login_data.get('login'):
        mis_login_list.append((i.get('username'), i.get('pwd'), i.get('yzm'), i.get('exp')))
    print(mis_login_list)
    return mis_login_list


class TestLogin:

    def teardown_class(self):
        Driver.quit_tp_driver()

    @pytest.mark.parametrize('username,pwd,yzm,exp', mis_login_data())
    def test_login(self, username, pwd, yzm, exp):
        logging.info('后台管理登录:username:{},pwd:{},yzm:{},exp:{}'.format(username, pwd, yzm, exp))
        Page.get_tp_login().login_page(username, pwd, yzm)
        # 断言
        assert Page.get_tp_login().page_exits_text(exp)
