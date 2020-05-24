# #定义多个参数，让函数可以处理多个参数
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# # 以上代码可以计算x的任意数量平方根，但是如果只需要常见的二次平方，就可以用以下写法：
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))
# print(power(5,2))
# print(power(5,5))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll("leo","b"))
print("转折")
print(enroll("leo","b",15))
