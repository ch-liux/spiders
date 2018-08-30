'''
Created on 2018年8月5日

@author: Administrator
'''

"""
获取对象信息
"""
import types

print(type(123))
print(type(None))

print(type(abs))

class Animal(object):
    pass
print(type(Animal()) == Animal)

def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

class Dog(Animal):
    def __len__(self):
        return 100
class Husky(Dog):
    pass
print(isinstance(Husky(), Dog))
print(isinstance(Husky(), Animal))
print(isinstance(Dog(), Husky))

print(isinstance([1,3,5], (list, tuple)))
a = "abc0"
print(dir(a))
print(a.__len__())
a.__add__("gg")
print(a)

l = Dog()
print(l.__len__())
print(len(l))
print(len("123"))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
my = MyObject()
print(hasattr(my, 'x'))
setattr(my, "x", 99)
print(getattr(my, 'x'))
setattr(my, 'y', 1)
print(my.__dict__)
try:
    getattr(my, 'z')
except AttributeError:
    print("no attr")
print(getattr(my, 'z', 40))
oop = getattr(my, 'power')
print(oop)
print(oop())
print(hasattr(my, 'read'))
print(hasattr("123", "read"))
    