'''
Created on 2018年8月4日

@author: Administrator
'''

"""
继承和多态
"""
class Animal(object):
    def run(self):
        print("Animal is running")
class Dog(Animal):
    def run(self):
        print("Dog is running")
class Cat(Animal):
    pass
dog = Dog()
dog.run()
Animal().run()
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
a = Animal()
print(isinstance(a, Dog))

def run_twice(obj):
    print(type(obj))
    obj.run()

# run_twice("123")
run_twice(Animal())
run_twice(Dog())
