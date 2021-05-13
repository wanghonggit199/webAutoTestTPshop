"""
登录---测试用例
"""
from parameterized import parameterized
import json
import unittest
import time

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utlis import DriverUtil
import logging

def read_bulid_data():
    # with open("../data/login_data.json", encoding="utf-8") as f:
    with open(BASE_DIR + "\data\login_data.json", encoding="utf-8") as f:
        data = json.load(f)
        # 声明一个空列表
        data_list = list()
        for i in data.values():
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('code'),
                              i.get('expect')))
        logging.info(data_list)
        return data_list


class TestLogin(unittest.TestCase):
    """登录测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务对象
        cls.login_proxy = LoginProxy()  # 登录业业务对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get("http://localhost/")  # 打开首页
        self.index_proxy.go_to_login()  # 点击登录链接

    @parameterized.expand(read_bulid_data)
    def test_login(self, userame, password, code, expect):
        """登录测试方法"""
        self.login_proxy.login(userame, password, code)  # 实现登陆
        time.sleep(3)
        title = self.driver.title  # 获取登录标题信息
        logging.info(title)
        try:
            self.assertIn(expect, title)  # 设置断言
        except AssertionError as e:
            # 截图
            self.driver.get_screenshot_as_file(BASE_DIR + "/screenshot/login_assert" + time.strftime("%Y%m%d-%H%M%S") + ".png")
            raise e


if __name__ == '__main__':
    unittest.main()
