# 将本py文件向解释器标注为utf-8
# -*- coding: utf-8 -*-


# 输出1+1
# print(1 + 1)

# print("hh")

# 赋予变量一个值，然后输出这个值
# name = input("请输入name：")
# print(name)

# name = input("请输入判断值：")
# if name > 10:
#     print("值大于10")
# else:
#     print("值小于10")


# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)


# # 同一个变量名称可以被反复赋值
# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)

# # 动态语言因为可以被反复赋值，所以等号的意义就变得更加灵活
# x = 1
# print(x)
# x = x + 1
# print(x)

# # 使用占位符向输出内容格式化插入内容
# print("XX%s,TT%s,HH%d"%("中文","en",2))

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# # print(str(n)+'\n'+str(f)+'\n'+s1+'\n'+s2+'\n'+s3+'\n'+s4)
# print(n,"\n",f,"\n",s1,"\n",s2,"\n",s3,"\n",s4)

# # print(11)
# # a = 11
# # print(a)
# # print(str(a))
# # print(int(a))

# print("转折点")

# x = 123
# print(x)


# age = input("in:")
# if age >= 18:
#     print("da")
# else:
#     print("x")

# age = 20
# if age >= 18:
#     print('your age is', age)
#     print('adult')

# print("%2d.%02d"%(3,1))


# s1 = int(input("first year:"))
# s2 = int(input("second year:"))
# r = (s2 - s1)/s1*100
# print(s1,s2,r)
# print("hi%.2fby"%(r))

# x = ['1','2','3']
# print(len(x))
# print("转折")
# a = len(x)
# print(a)

# print("插入一{0}插入二{1}".format(1,2))         

# a = ['1','2','3']
# print(a[1])
# print(a[-1])
# a.append('4')
# print(a[-1])

##################################################
# # 元组本身不可改变，但是元组指定的元素是可以改变的
# x = ['1','1']
# b = (1,2,x)
# print(b[2])
# x = ['2','2']
# b = (1,2,x)
# print(b[2])

################################################
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])


###########################################
# # 使用if else进行判断
# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('teenager')

##############################################
# #input输入的值是str字符串格式，如果想要对数字进行操作，需要使用int()函数将输入的值转化成整形
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


###########################################################
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
# 用if-elif判断并打印结果：
# height = 1.75
# weight = 80.5

# bmi = weight/(height**2)
# if bmi < 18.5:
#     print("你的体重过轻")
# elif 18.5 < bmi <25:
#     print("你的体重正常")
# elif 25 < bmi < 28:
#     print("你的体重过重")
# elif 28 < bmi < 32:
#     print("你的体重肥胖")
# elif bmi < 32:
#     print("你的体重严重肥胖")

# ###############################################
# # 依次输出每个名字
# L = ['Bart', 'Lisa', 'Adam']

# # for L in L:
# #     print(L)

# a = 0
# while a < len(L):
#     print("上面的打印",L[a])
#     a = a + 1
#     print('此时的a是：{0}'.format(a))

# # for i in L:
# #     print('hello,%s!'%i)

######################################################

# a = '123df2'
# for x in a:
#     print(x)

# #使用break语句结束循环
# n = 1
# while n<= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

# #使用continue语句跳过本次循环
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 ==0:
#         continue
#     print(n)

# # ##创建并输出字典内容
# a = {'tang':1995,'jia':12,'cheng':23}
# # print(a['tang'])
# print("第一次：{0}".format(a['tang']))

# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 | s2)

# d = {
#     'Michael' : 95,
#     'Bob' : 75,
#     'Tracy' : 85
# }
# print(d.get('thomas',-1))
# print('转折')
# print("此人的成绩是：",d.get('thomas',"查无此人,无法查询成绩"))

# l = ['ad','Bd','cd']
# L = []
# Nu = input('新用户名：')
# x = 0
# while x < len(l)-1:
#     if Nu.lower() == l[x].lower():
#         pass
#     else:
#         L.append(Nu)
#     x = x + 1
# print(L)
# ########################
# for x in l:
#     L.append(x.lower())
# # print(L)
# ######################
# if Nu.lower() in L:
#     print('您的用户名已被占用')
# else:
#     L.append(Nu)
# print(L)










# for L in l:
#     # print(Nu.lower())
#     # print(L.lower())
#     # print('分隔符---')
#     if L.lower() in l:
#         print('您的用户名已被占用')
#     else:
#         l.append(Nu)
# print(l)
# print('分隔符-------')
# Nu = input('新用户名：')
# for L in l:
#     if L.lower == Nu.lower:
#         print('您的用户名已被占用')
#     else:
#         l.append(Nu)





# alien_0 = {'x_position':0, 'y_position':25, 'speed':'fast'}
# print("Original x_position: " + str(alien_0['x_position']))
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_positon'] = alien_0['x_position'] + x_increment
# print("new x_position: " + str(alien_0['x_position']))

print("aaa\naaa","ccc")