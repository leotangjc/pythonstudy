# -*- coding: utf-8 -*-



# ' a test module '

# __author__ = 'Michael Liao'

# import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()

# class Student(object):
#     pass

# bart = Student()
# print(bart)

# class ppap():
#     pass

# print(type(ppap))

# class Animal():
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running..')

# def run_twice(animal):
#     animal.run()
#     animal.run()

# print(run_twice(Dog()))
# 对于静态语言（例如 Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于 Python 这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了

# 这就是动态语言的 “鸭子类型”，它并不要求严格的继承体系，一个对象只要 “看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# 求绝对值的函数abs
# print(abs(-100))

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

def pf(x,n):
    while n > 0:
        n -= 1
        x *= x
        
    return x
print(pf(3,2))
