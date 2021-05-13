"""
商品详情页
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utlis import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情对象层"""

    def __init__(self):
        super().__init__()

        self.add_cart = (By.ID, "join_cart")  # 购物车按钮
        self.add_cart_result = (By.CSS_SELECTOR, '.conect-title')  # 购物车添加文本元素

    def find_add_cart_btn(self):
        """添加到购物车按钮元素"""
        return self.find_element_func(self.add_cart)

    def find_add_cart_result(self):
        """定位获取加入购物车结果元素"""
        return self.find_element_func(self.add_cart_result)


class GoodsDetailHandle(BaseHandle):
    """商品详情操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_add_cart_btn(self):
        """点击添加到购物车按钮方法"""
        self.click_element(self.goods_detail_page.find_add_cart_btn())

    def get_add_cart_result(self):
        """获取加入购物车结果方法"""
        driver = DriverUtil.get_driver()
        # 切换frame
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        return self.goods_detail_page.find_add_cart_result().text


class GoodsDetailProxy(object):
    """商品详情业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    def add_cart_func(self):
        """添加商品到购物车方法"""
        self.goods_detail_handle.click_add_cart_btn()

    def get_add_cart_text_func(self):
        """获取购物车添加成功文本信息方法"""
        return self.goods_detail_handle.get_add_cart_result()
