# -*- coding: utf-8 -*-

# 想要使用unittest的话，创建类的时候，要继承unittest




import unittest
import json
import HTMLTestRunner
from base import RunMain

class TestMethod(unittest.TestCase):
    #  所有的case都必须由test开头，不然无法执行

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://....'
        data = {
        'username':'mushishi',
        'passwoed':'111111'
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)

        # 通过返回字典中的状态码，来判断是否通过测试
        # if res['errorCode'] == 1000:
        #     print('测试通过')
        # else:
        #     print('测试失败')

        # 也可以同断言语句重构上述语句
        self.assertEqual(res['errorCode'], 1000, '测试失败')
 

if __name__ == '__main__':
    unittest.main()



