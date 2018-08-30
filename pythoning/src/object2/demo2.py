'''
Created on 2018年8月5日

@author: Administrator
'''
"""
使用@property
"""
# class Student(object):
#     pass
# s = Student()
# s.score = 999

# class Student(object):
#     def set_score(self, score):
#         if not isinstance(score, int):
#             raise ValueError("score not is int")
#         if score <0 or score> 100:
#             raise ValueError("score 0-100")
#         self.score = score
#     def get_score(self):
#         return self.score
# s = Student()
# s.set_score(66)
# print(s.get_score())

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, score):
#         if not isinstance(score, int):
#             raise ValueError("score not is int")
#         if score <0 or score> 100:
#             raise ValueError("score 0-100")
#         self._score = score
# s = Student()
# s.score = 9
# print(s.score)

class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2018-self._birth
s = Student()
s.birth = 1994
print(s.birth)
print(s.age)