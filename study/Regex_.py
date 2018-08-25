
# 正则表达式

import re

content = 'Hello 123 4567 World_This a Regex Demo'

# 常规匹配
r = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(len(content))
print(r)
print(r.group())
print(r.span())

# 泛匹配
r = re.match("^Hello.*Demo$", content)
print(len(content))
print(r)
print(r.group())
print(r.span())


# 目标匹配 
content = 'Hello 1234567 World_This a Regex Demo'
r = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
print(len(content))
print(r)
print(r.group(1))
print(r.span())

# 贪婪匹配
content = 'Hello 1234567 World_This a Regex Demo'
r = re.match('^He.*(\d+).*Demo$', content)
print(r.group(1))
# 非贪婪匹配
content = 'Hello 1234567 World_This a Regex Demo'
r = re.match('^He.*?(\d+).*Demo$', content)
print(r.group(1))
# 匹配模式
content = """hello 1234567 World_This
is a  Demo
"""
r = re.match("^.*?(\d+).*?", content, re.S)
print(r.group(1))

# 转义
content = 'price is $500.00'
r = re.match("price is \$500.00",content)
print(r)

#
# 总结：
# 尽量使用泛匹配、使用括号得到匹配目标、尽量使用非贪婪模式、有换行符就用re.S
#


# re.search
# 能用search就不用match
content = "<_sre.SRE_Match object; span=(0, 16), match='price is $500.00'>"
r = re.match('object.*?(\d+).*?', content)
print(RuntimeWarning)
r = re.search('object.*?(\d+).*?', content)
print(r.group(1))

# 演练
# re.findall('', content)
re.findall('<li.*?>\s*?(<a.*?>?(\w+)(</a>)?\s*?</li>)',content)

# re.sub
# 替换
c = re.sub('\d+', '', content)
print(c)

# re.compile()
# 将字符串编译成正则

re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)





