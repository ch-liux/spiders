'''
Created on 2018年8月21日

@author: Administrator
'''

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>hello, web!</h1>']


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # environ['HTTP_USER_AGENT']:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
    # environ['PATH_INFO']:/abc/123
    # environ['SERVER_PORT']：8000
    # environ['SERVER_PROTOCOL']:HTTP/1.1
    # environ['QUERY_STRING']:a=1&b=1
    # environ['REMOTE_ADDR']:127.0.0.1
    # environ['CONTENT_TYPE']:text/plain
    # environ['HTTP_HOST']:localhost:8000
    # environ['HTTP_ACCEPT']:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    # environ['HTTP_COOKIE']:__guid=111872281.1145913981461973600.1531965568249.1638; monitor_count=9
    # environ['HTTP_ACCEPT_LANGUAGE']:zh-CN,zh;q=0.9
    # environ['REQUEST_METHOD']:GET
    return [body.encode('utf-8')]
