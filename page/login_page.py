"""
登录页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录对象库层"""
    def __init__(self):
        super().__init__()  # 获取父类方法中的浏览器对象

        self.username = (By.ID, 'username')  # 用户名
        self.password = (By.ID, "password")  # 密码
        self.verify_code = (By.ID, "verify_code")  # 验证码
        self.login_btn = (By.NAME, "sbtbutton")  # 登录按钮

    def find_username(self):
        """用户名定位方法"""
        return self.find_element_func(self.username)

    def find_password(self):
        """密码框定位方法"""
        return self.find_element_func(self.password)

    def find_verify_code(self):
        """验证码定位方法"""
        return self.find_element_func(self.verify_code)

    def find_login_btn(self):
        """登录按钮定位方法"""
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    """登录页面操作层"""
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        """用户名输入方法"""
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, password):
        """密码输入方法"""
        self.input_text(self.login_page.find_password(), password)

    def input_verify_code(self, code):
        """验证码输入方法"""
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        """登录按钮点击方法啊"""
        self.click_element(self.login_page.find_login_btn())


class LoginProxy(object):
    """登录页面---业务库层---(封装测试业务方法)"""

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, password, code):
        """登录方法"""
        self.login_handle.input_username(username)  # 输入用户名
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.input_verify_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录
