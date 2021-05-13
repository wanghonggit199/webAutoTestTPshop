"""
订单测试用例
"""
import json
import unittest

import time

from config import BASE_DIR
from page.goods_cart_page import GoodsCartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_check_page import OrderCheckProxy
from page.order_pay_page import OrderPayProxy
from utlis import DriverUtil, get_tip_text, switch_new_window
from parameterized import parameterized
import logging


def read_order_data():
    with open(BASE_DIR + "/data/order_data.json", encoding="utf-8") as f:
        data = json.load(f)
        # 声明一个空列表
        data_list = list()
        for i in data.values():
            data_list.append((
                              i.get('expect')))
    return data_list


class TestOrder(unittest.TestCase):
    """"订单测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 初始化浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.goods_cart_proxy = GoodsCartProxy()  # 购物车业务执行对象
        cls.order_check_proxy = OrderCheckProxy()  # 订单确认业务执行对象
        cls.my_order_proxy = MyOrderProxy()  # 我的订单页面业务执行对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付页面业务执行对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()  # 关闭浏览器

    def setUp(self):
        self.driver.get("http://localhost/")

    @parameterized.expand(read_order_data)
    def test_1order(self, expect):
        self.index_proxy.go_to_goods_cart()  # 跳转我的购物车
        self.goods_cart_proxy.go_to_order_check_func()  # 跳转确认订单页面方法
        time.sleep(5)
        self.order_check_proxy.submit_order_func()  # 提交订单方法
        # 获取订单结果
        result = get_tip_text(expect)
        # 设置断言
        try:
            self.assertTrue(result)
        # 截图
        except AssertionError as e:
            self.driver.get_screenshot_as_file(BASE_DIR + "/screenshot/order_check_assert" + time.strftime("%Y%m%d-%H%M%S") + ".png")
            raise e

    @parameterized.expand(read_order_data)
    def test_2order_pay(self, expect):
        """订单支付测试"""
        self.index_proxy.go_my_order_func()  # 点击订单支付
        # 切换新窗口
        switch_new_window()

        self.my_order_proxy.go_to_order_pay()  # 点击立即支付
        # 切换新窗口
        switch_new_window()

        self.order_pay_proxy.order_pay_func()  # 确认支付方式
        result = get_tip_text(expect)  # 获取支付结果
        try:
            self.assertTrue(result)  # 设置断言
        except AssertionError as e:
            self.driver.get_screenshot_as_file(BASE_DIR + "/screenshot/order_pay_assert" + time.strftime("%Y%m%d-%H%M%S") + ".png")
            raise e


if __name__ == '__main__':
    unittest.main()
