# -*- coding: utf-8 -*-

# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


def dan(a, b):
    if a%2 == 1:
        while a < b:
            a += 2
            print(a)
    else:
        while a < b:
            a += 2
            print(a)

print(dan(2, 14))