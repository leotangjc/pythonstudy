# -*- coding: utf-8 -*-
import re

a = 'abc|bac|cba|adc123callbsdiiikkkxy11we1cvb'

# x = re.findall('cba',a)
# y = re.findall('cab',a)

# if len(x) > 0:
#     print('字符串中包括：' , x)
# else:
#     print('字符串不中包括：' , x)

# if len(y) > 0:
#     print('字符串中包括：' , y)
# else:
#     print('字符串不中包括：' , y)

# z1 = re.findall('c[bd]a',a)  # 正则匹配c与a之间夹杂b或d的字符
# z2 = re.findall('c[^bd]a',a)  # 正则匹配c与a之间不包括b或d的字符（取反）
# z3 = re.findall('[a-z]{3}',a) # 正则匹配连续三位的字符串
# z4 = re.findall('[a-z]+',a) # 正则匹配连续的字母
# print(z4)


b = 'python|pytho|pythonnxx|pp|xbpythonnnnnnnn'

z5 = re.findall('python*',b)
print(z5)
