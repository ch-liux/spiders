'''
Created on 2018年8月5日

@author: Administrator
'''
"""
定制类
"""

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return "Student object (name:%s)" % self.name
#     # __repr__()是为调试服务的
#     __repr__ = __str__
#     def __iter__(self):
#         return self
# s = Student('lmx')
# print(s.__str__)

# 斐波拉求数列
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()
# 方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# class Student(object):
#     def __init__(self):
#         self.a, self.b = 0,1  # 初始化两个计数器a，b
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         if self.a > 10000:
#             raise StopIteration()
#         return self.a
# for i in Student():
#     print(i)

# class Fib(object):
#     def __getitem__(self, n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# f = Fib()
# print(f[2])
# 
# print(list(range(100))[1:5])
# 
# class Fib(object):
#     def __getitem__(self, n):   #__setitem__/__delitem__
#         if isinstance(n, int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n, slice):# slice表示切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a,b=1,1
#             L = []
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                     a,b=b,a+b
#             return L
# f = Fib()
# print(f[:5])

# class Student(object):
#     def __init__(self):
#         self.name = 'lmx'
#     def __getattr__(self, value):
#         if value == 'score':
#             return 99
#         if value == 'age':
#             return lambda: 25
#         else:
# #             raise AttributeError("not exist attr \'%s\'" % value)
#             return None
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# print(s.abc)


# REST API
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain("%s/%s" % (self._path, path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
# print(Chain().status.user.timeline.list)
# print(Chain("status.user"))
# # print(Chain().users('lmx').repos)


class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('is %s' % self.name)
s = Student('lmx')
s()

print(callable(s))
print(callable(int))
print(callable('123'))



