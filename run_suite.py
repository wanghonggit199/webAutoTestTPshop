"""
测试套件组装
"""

import unittest
import time
from case.test_cart import TestCart
from case.test_login import TestLogin
from case.test_order import TestOrder
from config import BASE_DIR
from utlis import DriverUtil
from tools.HTMLTestRunnerCN import HTMLTestReportCN

suite = unittest.TestSuite()  # 初始化套件对象
# 关闭浏览器退出方法
DriverUtil.chang__quit_status(False)
# 调用方法测试用例
suite.addTest(unittest.makeSuite(TestLogin))  # 登录
suite.addTest(unittest.makeSuite(TestCart))  # 添加商品
suite.addTest(unittest.makeSuite(TestOrder))  # 提交订单

# 初始化执行对象并调用方法
# unittest.TextTestRunner().run(suite)
# 设置报告存放路径及文件名
report_file = BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 打开报告写入文件流
# 注意: wb 以二进制形式写入内容到文件
with open(report_file, "wb") as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='HPShop 自动化测试报告',
                              description='系统:Windows 浏览器:谷歌 编程语言:Python',
                              tester='QA')
    # 调用执行方法生成测试报告
    runner.run(suite)
time.sleep(5)

DriverUtil.chang__quit_status(True)  # 打开浏览器
# 退出浏览器对象
DriverUtil.quit_driver()
