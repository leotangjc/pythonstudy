# -*- coding: utf-8 -*-


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
# 	print('step 1')
#     yield 1
#     print('step 2')
#     yield (3)
#     print('step 3')
#     yield (5)
# o = odd()
# for x in o:
#     print(x)

#迭代器
#可以直接作用于for循环的对象统称为可迭代对象:iterator
# 使用isinstance()可以判断一个对象是否是可迭代对象iterator
    # 集合数据elixir，和generator(生成器)是可迭代的
# from collections import Iterable
# print(isinstance([], Iterable))
#可以被next()函数调用，并不断返回下一个之的对象成为迭代器：iterator
# 凡是可作用于for循环的对象都是iterable类型
# for循环的本质就是不断调用next()函数实现的


#函数式编程

# 函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# 高阶函数
        # 变量可以指向函数
            # 例如求绝对值的函数abs
            # 可以将此函数指向变量
            # a = abs
            # print(a(-30))
        # 函数名也是变量
        	# 函数名就是指向函数的变量
		# 传入函数
			# 既然变量可以指向函数，函数的参数能结婚搜变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称为高阶函数
			# def add(x, y, f):
			# 	return f(x) + f(y)
			# print(add(-5, 6, abs))

# map/reduce
	# map
		# map()函数接收两个参数，一个是函数，一个是Iterable(迭代器)，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator(迭代器)返回。
		# def f(x):
		# 	return x * x
		# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
		# print(list(r))
		# print(r)
	# reduce
		# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
		# 比如序列求和
		# from functools import reduce
		# def add(x, y):
		# 	return x + y
		# print(reduce(add, [1, 3, 5, 7, 9]))
# filter()
	# 内置的filter()函数用来过滤序列
	# filter()接收一个函数和一个序列。根据返回值是True还是False决定保留还是丢弃该元素
	# 保留奇数：
	# def is_odd(n):
	#     return n % 2 == 1
	# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
	# 删除空字符串：
	# def not_empty(s):
	#     return s and s.strip()
	# list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# sorted
	# 排序算法
		# sorted()函数可以直接进行排序：
			# print(sorted([36, 5, -12, 9, -21]))
		# 这个高阶函数也可以接受一个key函数来实现自定义的排序
			# print(sorted([36, 5, -12, 9, -21], key=abs))
			
		
# 返回函数
	# 函数作为返回值
		# ps:将函数作为返回值的时候，应该是将函数和需要的参数共同赋予了返回值，需要执行彩灯得到结果。此行为也被称为“闭包”
	# 闭包

# 匿名函数
	# lambda
	# 例：
	# list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
	# 匿名函数只能有一个表达式


# 装饰器
# 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数。
	# decorator
	# 例：
	# def outer(some_func):
	#     def inner():
	#         print("before some_func")
	#         ret = some_func()
	#         return ret + 1
	#     return inner
	# @outer
	# def foo():
	#     return 1
	# print(foo())
	# # decorated = outer(foo)
	# # print(decorated())


# 模块
	# 把函数分组，放到不同的文件里，每个文件就是一个模块
	# 	把一个分类的文件放在一个文件夹里，这个目录就叫包(package)
	#	每个包目录下都需要有一个__init__.py文件，有这个文件存在，就会被Python识别成一个包，这个文件可以是空文件，也可以有Python代码
	# 使用import导入模块


# 面向对象
	# 类和实例
		# 类是抽象的模板
		# 实例是根据类创建除了的具体的对象，每个生成的对象都拥有相同的方法，但各自的数据可能不同
		# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个__init__方法，在创建实例的时候，把属性绑定上去
			# __init__方法的第一个参数永远是self，表示创建的实例本身。因此，在创建实例的时候，必须要传入与__init__方法匹配的参数
		# 数据封装
			# 可以通过类内部定义访问数据的函数，这些函数是和类本身关联起来的，这样就把数据封装起来了，称为类的方法
			# class Student(object):
			# 	def __init__(self, name, score):
			# 		self.name = name
			# 		self.score = score
			# 	def print_score(self):
			# 		print('%s: %s' % (self.name, self.score))
			# bart = Student('Bart Simpson', 59)
			# print(bart.print_score())
	#访问限制
		# 在没有进行访问限制时，从外部是可以直接对内部属性进行修改的，如：
			# bart.score = 99
		# 如果想让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，使其变为一个私有变量，只有内部可以访问
		# 想要让对象允许从外部修改的话，可以增加一个set_score方法，这样做的优点是，可以在这个方法中，可以对参数进行检查，避免传入无效参数
	# 继承和多态
		# 当我们定义一个class的时候，可以从现有的class继承，新的class称为子类，被继承的称为基类、父类
		# 继承的好处就是子类获得了父类的全部功能
		


