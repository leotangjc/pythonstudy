# -*- coding: utf-8 -*-
# 假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
# l=['Adam','95.5','Lisa','85','Bart','59']
# print(l)

# 三名同学的成绩可以用一个list表示：
# L = [95.5, 85, 59]
# # 请按照索引分别打印出第一名、第二名、第三名，同时测试 print L[3]。
# L = [95.5, 85, 59]
# print(L[0])
# print(L[1])
# print(L[2])
# print(L[3])

# 三名同学的成绩可以用一个list表示：
# L = [95.5, 85, 59]
# 请按照倒序索引分别打印出倒数第一、倒数第二、倒数第三。
# L = [95.5, 85, 59]
# print(L[-1])
# print(L[-2])
# print(L[-3])

# 假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
# l=['Adam','Lisa','Bart']
# l.insert(2,'Paul')
# print(l)

# 注意右边编辑器代码中 list 如下：
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# Paul的索引是2，Bart的索引是3，如果我们要把Paul和Bart都删掉，请解释下面的代码为什么不能正确运行：
# L.pop(2)
# L.pop(3)
# 怎样调整代码可以把Paul和Bart都正确删除掉
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# L.pop(2)
# L.pop(2)

# 班里的同学按照分数排名是这样的：
# L = ['Adam', 'Lisa', 'Bart']
# 但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。
# 请通过对list的索引赋值，生成新的排名。
# L = ['Adam', 'Lisa', 'Bart']
# L[0]='bart'
# L[2]='Adam'
# print(L)


# 创建一个tuple，顺序包含0 - 9这10个数。
# A = (0,1,2,3,4,5,6,7,8,9)
# print(A)

# 请指出右边编辑器中代码为什么没有创建出包含一个学生的 tuple：
# t = ('Adam')
# print t
# 请修改代码，确保 t 是一个tuple。
# t = ('Adam',)
# print(t)

# 定义了tuple：
# t = ('a', 'b', ['A', 'B'])
# 由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
# t = ('a', 'b', 'A', 'B')
# print(t)

# 如果成绩达到60分或以上，视为passed。
# 假设Bart同学的分数是75，请用if语句判断是否能打印出 passed:
# bart=75
# if bart > 60:
#     print('passed')


# 如果成绩达到60分或以上，视为passed，否则视为failed。
# 假设Bart同学的分数是55，请用if语句打印出 passed 或者 failed:
# bart = 55
# if bart >60:
#     print('passed')
# else:
#     print('failed')


# 如果按照分数划定结果：
#     90分或以上：excellent
#     80分或以上：good
#     60分或以上：passed
#     60分以下：failed
# 请编写程序根据分数打印结果。
# bart = 65
# if bart >90:
#     print('excellent')
# elif bart>80:
#     print('good')
# elif bart>60:
#     print('passed')
# elif bart<60:
#     print('failed')


# 班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：
# L = [75, 92, 59, 68]
# 请利用for循环计算出平均成绩。
# L = [75, 92, 59, 68]
# a=0.0
# c=0
# for b in L:
#     a=a+b
#     c=c+1
# print (a/c)


# 利用while循环计算100以内奇数的和。
# sum = 0
# x = 1
# while x <= 100:
#     sum = sum + x
#     x = x+2
# print

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
# sum=0
# x=1
# n=1
# while True:
#     n=n+1
#     sum=sum+x
#     x=x*2
#     if n > 20 :
#         break
# print(sum)

# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
# # sum = 0
# # x = 1
# # while True:
# #     sum = sum + x
# #     x = x + 1
# #     if x > 100:
# #         break
# # print sum
# sum = 0
# x = 0
# while True:
#     x = x + 1
#     if x > 100:
#         break
#     if x % 2 == 0:
#         continue
#     sum = sum + x
# print(sum)


# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
# for x in [1, 2, 3, 4, 5, 6, 7, 8]:
#     for y in [2, 3, 4, 5, 6, 7, 8, 9]:
#         if x < y:
#             print (x*10+y)


# 新来的Paul同学成绩是 75 分，请编写一个dict，把Paul同学的成绩也加进去。
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59,
#     'Paul': 75
#     }
# print(d)


# 根据如下dict：
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# 请打印出：
# Adam: 95
# Lisa: 85
# Bart: 59
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# for (key, value) in d.items():
#     print("%s: %s" % (key, value))


# 请设计一个dict，可以根据分数来查找名字，已知成绩如下：
# Adam: 95,
# Lisa: 85,
# Bart: 59.
# d = {
#     95: 'Adam',
#     85: 'Lisa',
#     59: 'Bart'
#     }
# a=input('c:')
# print(d[a])


# 请根据Paul的成绩 72 更新下面的dict：
# d = {
#     95: 'Adam',
#     85: 'Lisa',
#     59: 'Bart'
# }
# d = {
#     95: 'Adam',
#     85: 'Lisa',
#     59: 'Bart'
# }
# d[72]='Paul'
# print(d)


# 请用 for 循环遍历如下的dict，打印出 name: score 来。
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# for a in d:
#     print("%s: %s" % (a, d[a]))


# 请用set表示班里的4位同学：
# Adam, Lisa, Bart, Paul
# a = set(['Adam', 'Lisa', 'Bart', 'Paul'])
# print(a)


# 由于上述set不能识别小写的名字，请改进set，使得 'adam' 和 'bart'都能返回True。


# 请用 for 循环遍历如下的set，打印出 name: score 来。
# s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
# s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
# for x in s:
#     print(x)


# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# s = set(['Adam', 'Lisa', 'Paul'])
# s.add('Bart')
# print(s)
