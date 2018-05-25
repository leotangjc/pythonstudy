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

# def pf(x,n):
#     s = 1
#     while n > 0:
#         n -= 1
#         s *= x

#     return s
# print(pf(3,2))


# 默认参数
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))
# print(power(5，3))
# 在使用这个函数时，如果不设置第二个参数，就会使用默认的‘n=2’，也就是默认输出平方数
# 必选参数需要在前，默认参数在后
# 默认参数必须指向不变对象


# 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3,4))
# 对传入参数前附加*符号，可将其变为可变参数，使其变为一个tuple


# 关键字参数
# def person(name,age,**kw):
#     return('name:',name,'age:',age,'other:',kw)
# print(person('leo', 23))
# print(person('tjc', 21, city='shiyan'))


# 命名关键字参数


# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, *y):
#     s = 1
#     s *= x
#     for z in y:
#         s *= z
#     return s


# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))


# 切片
# a[起始下标:间隔数:终点下标]
#练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
# def trim(a):
#     lens = len(a)
#     if a[:1] == ' ':
#         a = a[1:]
#         return trim(a)
#     elif a[-1:] == ' ':
#         a = a[:lens-1]
#         return trim(a)
#     else:
#         return a




#迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 默认情况下，dict迭代的是key。 如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# Python内置的enumerate函数可以把一个list变成索引-元素对



#列表生成式
# # 想要生成[1x1, 2x2, 3x3, ..., 10x10]的话，可以使用列表生成式
# print([x * x for x in range(1, 11)])
# # 也可以附加if判断，如筛选出偶数的平方
# print([x * x for x in range(1, 11) if x % 2 == 0])
# 也可以实现两层循环
# print([m + n for m in 'ABC' for n in 'XYZ'])


# class s():
#     name = ''
#     age = 0
#     def __init__(self,name,age):
#         name = name
#         age = age


# 生成器（generator)
# 把列表生成式的[]改成()，就创建了一个generator：
# g = (x * x for x in range(10))
# for n in g:
#     print(n)
# 通常我们使用for循环来迭代generator
# 如斐波拉契数列，出第一个和第二个数歪，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# # print(fib(12))
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield (3)
#     print('step 3')
#     yield (5)
# o = odd()
# for x in o:
#     print(x)

#迭代器
#可以直接作用于for循环的对象统称为可迭代对象:lterabld
# 使用isinstance()可以判断一个对象是否是可迭代对象lterable
