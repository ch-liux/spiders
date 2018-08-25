
# PyQuery
# 
from pyquery import PyQuery as pq
html = """
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <title>layui在线调试</title>
  <link rel="stylesheet" href="//res.layui.com/layui/dist/css/layui.css?t=1531663423583" media="all">
  <style>
    body{margin: 10px;}
    .demo-carousel{height: 200px; line-height: 200px; text-align: center;}
  </style>
</head>
<body>
 
<table class="layui-hide" id="test" lay-filter="demo"></table>
 
<script type="text/html" id="barDemo">
  <a class="layui-btn layui-btn-primary layui-btn-xs" lay-event="detail">查看</a>
  <a class="layui-btn layui-btn-xs" lay-event="edit">编辑</a>
  <a class="layui-btn layui-btn-danger layui-btn-xs" lay-event="del">删除</a>
</script>
 
<div class="layui-tab layui-tab-brief" lay-filter="demo">
  <ul class="layui-tab-title">
    <li class="layui-this">演示说明</li>
    <li>日期</li>
    <li>分页</li>
    <li>上传</li>
  </ul>
  <div class="layui-tab-content">
    <div class="layui-tab-item layui-show">
    
      <div class="layui-carousel" id="test1">
        <div carousel-item>
          <div><p class="layui-bg-green demo-carousel">在这里，你将以最直观的形式体验 layui！</p></div>
          <div><p class="layui-bg-red demo-carousel">在编辑器中可以执行 layui 相关的一切代码</p></div>
          <div><p class="layui-bg-blue demo-carousel">你也可以点击左侧导航针对性地试验我们提供的示例</p></div>
          <div><p class="layui-bg-orange demo-carousel">如果最左侧的导航的高度超出了你的屏幕</p></div>
          <div><p class="layui-bg-cyan demo-carousel">你可以将鼠标移入导航区域，然后滑动鼠标滚轮即可</p></div>
        </div>
      </div>
    </div>
    <div class="layui-tab-item">
      <div id="laydateDemo"></div>
    </div>
    <div class="layui-tab-item">
      <div id="pageDemo"></div>
    </div>
    <div class="layui-tab-item">
      <div class="layui-upload-drag" id="uploadDemo">
        <i class="layui-icon"></i>
        <p>点击上传，或将文件拖拽到此处</p>
      </div>
    </div>
  </div>
</div>
"""
# 字符串初始化
doc = pq(html)
# print(doc('li'))

# url初始化
doc = pq(url='http://www.baidu.com')
# print(doc('head'))

# 文件初始化
# with open('/demo.html', 'wb') as f:
#   f.write(str(html))
#   f.close
doc = pq(filename='demo.html')
# print(doc('li'))

# css选择器
doc = pq(html)
print(doc('#test1 div'))

# 查找元素
# 子元素
doc = pq(html)
items = doc('div')
print(type(items))
print(items)
lis = items.find('.layui-this')
print(lis)
print("-------------")
lis = items.children()
print(type(lis))
print(lis)
print("-------------")
lis = items.children('#uploadDemo')
print(lis)

print('-----------------')
# 父元素
doc = pq(html)
items = doc('.layui-this')
p = items.parent()
ps = items.parents()
print('****')
ps = items.parents('.layui-this')
print(p)
print(ps)

# 兄弟元素
s = items.siblings()
s = items.siblings('.layui-this')

# 遍历
# 单个元素
items = doc('.layui-this')
# 多个元素
items = doc('.layui-this').items()
print(type(items))
for item in items:
  print(item)


# 获取信息
# 获取属性
doc = pq(html)
a = doc('table')
print(a.attr('id'))
# 获取文本
a = doc('li')
print(a.text())
print(type(a.text()))
# 获取html
print(a.html())

# dom操作
a.removeClass('.layui')
a.addClass('.layui')
a.attr('name', 'link')  #加一个name=link
a.css('font-size', '14px')  #加一个font-size：14的style
a.remove()
a.find('p').remove()

# pyQuery api

# 伪选择器 css3
doc = pq(html)
li = doc('li:first-child')
li = doc('li:last-child')
li = doc('li:nth-child(2)')
li = doc('li:gt(2)')  #第二个以后的元素
li = doc('li:nth-child(2n)')  #偶数个
li = doc('li:contains(second)') #包含second的元素




