# 请求上下文环境
from flask import Flask, g, request


app = Flask(__name__)


@app.before_request
def before_request():
    print("before request start")
    print(request.url)


@app.before_request
def before_request2():
    print("before request start 2")
    print(request.url)
    g.name = "SampleApp"


@app.after_request
def after_request(response):
    print("after request start")
    print(request.url)
    response.headers['key'] = 'value'
    return response


@app.teardown_request
def teardown_request(exception):
    # 此处，没有exception会报异常
    print("teardown request")
    print(request.url)


@app.route("/")
def index():
    return "Hello, %s!" % g.name


if __name__ == '__main__':
    app.run()