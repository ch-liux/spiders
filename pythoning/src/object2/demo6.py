'''
Created on 2018年8月6日

@author: Administrator
'''

"""
使用元类
"""

# class Hello(object):
#     def hello(self, name='world'):
#         print("hello %s" % name)
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
# print()

# 使用type可以动态创建class
# def fn(self, name='world'):
#     print("hello %s" % name)
# Hello = type("Hello", (object,), dict(hello=fn))
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass是类的模板，所以必须从`type`类型派生
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
# class MyList(list, metaclass=ListMetaclass):
#     pass
# L = MyList()
# L.add(1)
# L.append(2)
# print(L)


# 测试ORM  
class Field(object):
    def __init__(self, name, colnum_type):
        self.name = name
        self.colnum_type = colnum_type
    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print("found model %s" % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print("found mapping %s ==> %s" % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name           # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' has no attr '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:%s' % sql)
        print('args:%s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=123456, name="lmx", email='163@com', password="123456")
u.save()


