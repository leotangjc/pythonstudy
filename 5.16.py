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

class Animal():
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def run_twice(animal):
    animal.run()
    animal.run()
    