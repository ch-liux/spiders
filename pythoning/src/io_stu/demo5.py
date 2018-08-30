'''
Created on 2018年8月13日

@author: Administrator
'''

"""
序列化
"""

# u = dict(name='lmx', age=20, score=75)
# print(u)
# 
# import pickle
# print(pickle.dumps(u))
# 
# f = open('test.txt', 'wb')
# pickle.dump(u, f)
# f.close()
# 
# f = open('test.txt', 'rb')
# u = pickle.load(f)
# f.close
# print(u)

import json
u = dict(name='lmx', age=20, score=75)
print(json.dumps(u))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('lmx', 20, 30)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
    
s1 = json.dumps(s, default=student2dict)
print(s1)
print(json.dumps(u, default=lambda obj: obj.__dict__)) # 存在子类情况系
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s2 = json.loads(s1, object_hook=dict2student)
print(s2)

