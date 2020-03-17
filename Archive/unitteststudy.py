# -*- coding: utf-8 -*-

# 想要使用unittest的话，创建类的时候，要继承unittest





import unittest

class TestMethod(unittest.TestCase):
    #  所有的case都必须由test开头，不然无法执行

    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法')

    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')
        
    # 每次方法之前执行
    def setUp(self):
        print('test--->setUp')

    
    # 每次方法之后执行
    def tearDown(self):
        print('test--->tearDown')

    
    def test_01(self):
        print('这个是测试方法')

    def test_02(self):
        print('这个是2测试方法')

if __name__ == '__main__':
    unittest.main()






# import unittest
# class TestStringMethods(unittest.TestCase):
# def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
# def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
# def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
# if __name__ == '__main__':
#     unittest.main()
