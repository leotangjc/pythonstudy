# -*- coding: utf-8 -*-
# class Student():
#     name = ''
#     age = 0

#     def print_file(self)：
#     print('name:' + self.name)
#     print('age: ' + str(self.age))

# student = Student()
# student.print_file

class Student():
    name = ''
    age = 0

    def __init__(self, name, age):
        #构造函数
        name = name
        age = age
        print('student')

    def duo_homework(self):
        print('homework')

# class   Printer():
#     def print_file(self)：
#         print('name:' + self.name)
#         print('age: ' + str(self.age))


student1 = Student()
student1.__init__()
# student = Student()
# student.print_file



# “__init__”这个构造函数，具有初始化的作用，也就是当该类被实例化的时候就会执行该函数。那么我们就可以把要先初始化的属性放到这个函数里面。

# “__del__”就是一个析构函数了，当使用del 删除对象时，会调用他本身的析构函数，另外当对象在某个作用域中调用完毕，在跳出其作用域的同时析构函数也会被调用一次，这样可以用来释放内存空间。