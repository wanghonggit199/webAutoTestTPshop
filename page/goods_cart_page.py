"""
购物车页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class GoodsCartPage(BasePage):
    """购物车---对象层"""

    def __init__(self):
        super().__init__()
        self.check_all = (By.CLASS_NAME, "checkCartAll")  # 全选复选框
        self.go_check = (By.LINK_TEXT, "去结算")  # 去结算按钮

    def find_check_all(self):
        """全选框定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_check(self):
        """去结算按钮定位方法"""
        return self.find_element_func(self.go_check)


class GoodsCartHandle(BaseHandle):
    """购物车---操作层"""

    def __init__(self):
        self.goods_cart_page = GoodsCartPage()

    def click_check_all(self):
        """全选复选框点击方法"""
        check_all_element = self.goods_cart_page.find_check_all()
        # 判断复选框是否被选中
        if not check_all_element.is_selected():  # 如果没有被选中执行点击全选框操作
            self.click_element(check_all_element)

    def click_go_check(self):
        """去结算按钮点击方法"""
        self.click_element(self.goods_cart_page.find_go_check())


class GoodsCartProxy(object):
    """购物车---操作层"""

    def __init__(self):
        self.goods_cart_handle = GoodsCartHandle()  # 操作对象

    def go_to_order_check_func(self):
        """去订单确认页跳转方法"""
        self.goods_cart_handle.click_check_all()  # 确认全选
        self.goods_cart_handle.click_go_check()  # 去结算
