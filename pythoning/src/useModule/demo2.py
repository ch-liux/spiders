'''
Created on 2018年8月15日

@author: Administrator
'''

"""
collections"""

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(isinstance(p, Point), isinstance(p, tuple))
Circle = namedtuple('Circle', ['x', 'y', 'z'])

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('y')
q.appendleft('x')
q.append('xx')
q.pop()
q.popleft()
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key2'] = 123
print(dd['key1'], dd['key3'])

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
print(list(od.keys()))
print(list(od.values()))
ood = OrderedDict()
ood['x'] = 1
ood['y'] = 2
print(ood)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdateorderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateorderDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for i in 'testing':
    c[i] = c[i] + 1
print(c)

