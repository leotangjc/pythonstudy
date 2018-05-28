# -*- coding: utf-8 -*-

class testClass:
    def __init__(self, name, gender):
        self.Name = name  
        #self指的是一会创建类的实力的时候，这个被创建的实例本身
        #等号左边的Name是实例的属性，后面是方法__init__的参数
        self.Gender = gender
        print('hello')
        #在使用类创建实例的时候，__init__方法立刻被调用

testman = testClass('neo', 'male')
print(testman)
print('---')
print(testman.Name)
print('---')
print(testman.Gender)