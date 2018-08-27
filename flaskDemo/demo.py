from flask import Flask
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)
# app = Flask(__name__, static_folder='files')  #static_folder自定义静态文件目录位置


# @app.route('/')
# def index():
#     return "<h1>hello</h1>"


# @app.route('/hello/<name>')
# def hello(name):
#     return 'Hello %s ' % name


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello2(name=None):
    if name is None:
        name = 'World'
    else:
        return redirect(url_for('login'))
        # url_for('login')  # 返回/login
        # url_for('login', id='1')  # 将id作为URL参数，返回/login?id=1
        # url_for('hello', name='man')  # 适配hello函数的name参数，返回/hello/man
        # url_for('static', filename='style.css')  # 静态文件地址，返回/static/style.css
        # return u'这是测试'
    return 'Hello %s ' % name


@app.route('/user/<int:user_id>')
def get_user(user_id):
    return 'User ID: %d' % user_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'this is a post request'
    else:
        return 'this is a get request'


if __name__ == "__main__":
    # app.run() #默认 http://127.0.0.1:5000/
    app.run(host='127.0.0.1', port=8080, debug=True)