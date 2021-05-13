import json
import unittest
import time

from config import BASE_DIR
from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utlis import DriverUtil
from parameterized import parameterized
import logging


def read_cart_data():
    with open(BASE_DIR + "/data/cart_data.json", encoding="utf-8") as f:
        data = json.load(f)
        # 声明一个空列表
        data_list = list()
        for i in data.values():
            data_list.append((i.get('good_name'),
                              i.get('expect')))
    return data_list


# 此用例不可单独执行
class TestCart(unittest.TestCase):
    """购物车测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 商品搜索列表执行对象
        cls.search_list_proxy = SearchListProxy()  # 商品详情业务执行对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()  # 关闭浏览器对象

    def setUp(self):
        self.driver.get("http://localhost/")  # 打开首页

    @parameterized.expand(read_cart_data)
    def test_search_goods_go_tu_cart(self, good_name, expect):
        goods_name = good_name
        self.index_proxy.go_to_search_list(goods_name)  # 搜索 荣耀7
        time.sleep(3)
        self.search_list_proxy.go_to_goods_detail(goods_name)  # 点击搜索到的商品并跳转
        time.sleep(3)
        self.goods_detail_proxy.add_cart_func()  # 点击添加到购物车
        time.sleep(3)

        result = self.goods_detail_proxy.get_add_cart_text_func()  # 获取结果文本信息
        logging.info(result)
        try:
            self.assertIn(expect, result)  # 设置断言
        except AssertionError as e:
            # self.driver.get_screenshot_as_file("./screenshot/{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
            self.driver.get_screenshot_as_file(
                BASE_DIR + "/screenshot/cart_assert" + time.strftime("%Y%m%d-%H%M%S") + ".png")
            raise e


if __name__ == '__main__':
    unittest.main()
