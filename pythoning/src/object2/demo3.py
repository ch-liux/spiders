'''
Created on 2018年8月5日

@author: Administrator
'''
"""
多重继承
"""
class Animal(object):
    pass
class Dog(Animal):
    pass
class Bat(Animal):
    pass
class Parrot(Animal):
    pass
class Ostrich(Animal):
    pass

class Runnable(object):
    def run(self):
        print("running...")
class Flyable(object):
    def fly(self):
        print("flying...")

class Cat(Animal, Runnable):
    pass

c = Cat()
c.run()

# 网络服务:TCPServer/UDPServer
# 两种模型:ForkingMixIn/ThreadingMixIn
    
    
