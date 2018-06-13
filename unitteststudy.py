# -*- coding: utf-8 -*-

# 想要使用unittest的话，创建类的时候，要继承unittest

import unittest

class TestMethod(unittest.TestCase):
    #  所有的case都必须由test开头，不然无法执行

    def test_01(self):
        print('这个是测试方法')

    def test_02(self):
        print('这个是2测试方法')

if __name__ == '__main__':
    unittest.main()