"""
订单确认页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderCheckPage(BasePage):
    """订单确认---对象层"""

    def __init__(self):
        super().__init__()

        self.submit_order = (By.CLASS_NAME, "Sub-orders")

    def find_submit_order_btn(self):
        """提交订单按钮定位方法"""
        return self.find_element_func(self.submit_order)


class OrderCheckHandle(BaseHandle):
    """订单确认---操作层"""

    def __init__(self):
        self.order_check_page = OrderCheckPage()

    def click_order_check_btn(self):
        """点击提交订单按钮方法"""
        self.click_element(self.order_check_page.find_submit_order_btn())


class OrderCheckProxy(object):
    """订单确认---业务层"""

    def __init__(self):
        self.order_check_handle = OrderCheckHandle()

    def submit_order_func(self):
        """点击提交订单业务方法"""
        self.order_check_handle.click_order_check_btn()
