
# BeautifulSoup
# python标准库  BeautifulSoup(markup, 'html.parser')
# lxml html解析器   BeautifulSoup(markup, 'lxml')
# lxml xml解析器    BeautifulSoup(markup, 'xml')
# html5lib  BeautifulSoup(markup, 'html5lib')

# 基本使用
from bs4 import BeautifulSoup
html = """
<title>lxzy</title>
<li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30217981/?icn=index-latestbook-subject" title="故事经济学">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29797128.jpg" class=""
                  width="115px" height="172px" alt="故事经济学">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30217981/?icn=index-latestbook-subject"
                  title="故事经济学">故事经济学</a>
              </div>
              <div class="author">
                [美]罗伯特·麦基&nbsp;/&nbsp;[美]托马斯·格雷斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  故事经济学
                </h4>
                <p>
                  <span class="author">
                    [美]罗伯特·麦基&nbsp;/&nbsp;[美]托马斯·格雷斯
                  </span>
                  /
                  <span class="year">
                    2018-6
                  </span>
                  /
                  <span class="publisher">
                    天津人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  “为什么iPhone 的广告好，而Uber 的广告失败？”
好莱坞编剧教父罗伯特·麦基带领读者回归到广告时代开始的日子——富兰克林时代，从源头解析广告营销至今的兴衰历程，为困扰无数从业人员自从进入后广告时代开始“为什么人们不再相信广告？”这一究极问题寻找答案。
后广告时代的消费者们比起夸大其词和虚假承诺的广告，更加相信故事，而消费者们对于旧有广告模式的反...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30240991/?icn=index-latestbook-subject" title="下雨时蔷薇会开">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29786258.jpg" class=""
                  width="115px" height="172px" alt="下雨时蔷薇会开">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30240991/?icn=index-latestbook-subject"
                  title="下雨时蔷薇会开">下雨时蔷薇会开</a>
              </div>
              <div class="author">海棠</div>
              <div class="more-meta">
                <h4 class="title">
                  下雨时蔷薇会开
                </h4>
                <p>
                  <span class="author">
                    海棠
                  </span>
                  /
                  <span class="year">
                    2018-6
                  </span>
                  /
                  <span class="publisher">
                    湖南文艺出版社
                  </span>
                </p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
print(type(soup.a))
print(soup.a)
print(soup.span.attrs['class'])
print(soup.span['class'])
print(soup.div.a.img['alt'])
print(soup.div.contents)    #获取所有子节点
print(soup.div.children)    #获取所有子节点，迭代器
for i,child in enumerate(soup.div.children):
    print(i, child)
print(soup.p.descendants)   #获取子孙节点，迭代器
print(soup.p.parent)        #获取父节点
print(soup.p.parents)       #获取所有父节点，迭代器
print(list(enumerate(soup.p.parents)))  
print(soup.a.next_siblings) #获取下一个兄弟节点
print(soup.a.previous_siblings) #获取上一个兄弟节点
print(list(enumerate(soup.a.next_siblings))) 

# 标准选择器
# find_all(name, attrs, recurive, text,**kw)
print(soup.find_all('a'))
print(soup.find_all('a')[0])

print(soup.find_all(attrs={'class':'year'}))
print(soup.find_all(class_='year'))
print(soup.find_all(alt='下雨时蔷薇会开'))

print(soup.find_all(text='海棠'))

# find(name, attrs, recurive, text,**kw)
# find_parents()     find_parent()
# find_next_siblings()  find_next_sibling()
# find_previous_siblings()  find_previous_sibling()
# find_all_next()   find_next()
# find_all_previous()   find_previous()

# css选择器
print(soup.select('.publisher'))
print(soup.select('div h4'))
# 获取属性
# span['class']
# 获取内容
# span.get_text()

# 总结
# 推荐使用lxl解析库
# 处理速度快，查找存在局限性