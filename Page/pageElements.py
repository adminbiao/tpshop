from selenium.webdriver.common.by import By


class PageElements:
    """后台登录页面元素"""
    # 用户名 name : username
    username_name = (By.NAME, 'username')
    # 密码 name: password
    pwd_name = (By.NAME, 'password')
    # 验证码: css: input.chick_ue
    verification_code_css = (By.CSS_SELECTOR, 'input.chick_ue')
    # 登录 css: input.sub
    login_css = (By.CSS_SELECTOR, 'input.sub')
