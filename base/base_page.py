"""
PO 文件的基类
"""
from utlis import DriverUtil


class BasePage(object):
    """对象库基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element_func(self, location):
        """元素定位方法"""
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """操作层---基类"""

    @staticmethod
    def input_text(element, text):
        """
        元素输入方法
        :param element: 元素定位方法
        :param text: 要输入的文本
        :return:
        """
        element.clear()  # 一般输入前 先清空
        element.send_keys(text)

    @staticmethod
    def click_element(element):
        element.click()
