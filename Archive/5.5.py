# a = input()
# print('a is' + a)
# if a == 1:
#     print('apple')
# elif a == 2:
#     print('orange')
# elif a == 3:
#     print('banana')
# else:
#     print('shopping')
#运行错误的原因：键盘输入的数字不是数字，是字符串，所以输入时要转换格式
# a = int(input())
# if a == 1:
#     print('apple')
# elif a == 2:
#     print('orange')
# elif a == 3:
#     print('banana')
# else:
#     print('shopping'


a = [1,2,3,4,5,6,7,8]
for x in range(a[0],len(a),2):
    print(x)
    
import t.c7
print(t.c7.a)
#引用t目录下的c7模块
#输出此模块下的a变量

from t import c7
print(c7.a)
#从t目录（包）下，访问c7模块
#输出c7下的a变量

from t.c7 import (a,b,
c)
print(a)
print(b)
#从t目录（包）下的c7模块，引用所有
#输出c7下的a、b变量




