# 公共方法类
from selenium import webdriver
import time


def switch_new_window():
    """切换新窗口方法"""
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])  # 下标为 -1 的是新窗口


def get_tip_text(text):
    """获取文本结果信息的方法"""
    xpath = "// *[contains(text(), '{}')]".format(text)
    driver = DriverUtil.get_driver()
    try:
        element = driver.find_element_by_xpath(xpath)
        return element

    except Exception:
        return False


class DriverUtil(object):
    """浏览器驱动工具类"""
    _driver = None  # 保护变量 变量前添加一个下划线
    _quit_status = True

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了防止反复创建浏览器对象,需要对浏览器对象进行判断
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://localhost/")
        return cls._driver

    @classmethod
    def chang__quit_status(cls, status):
        """修改浏览器退出状态方法"""
        cls._quit_status = status

    @classmethod
    def quit_driver(cls):
        """退出浏览器的方法"""
        # if cls._driver is not None:
        if cls._driver and cls._quit_status:
            time.sleep(3)
            cls._driver.quit()
            cls._driver = None  # 此代码确保浏览器对象会被从内存中移除掉


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(3)
    DriverUtil.quit_driver()
