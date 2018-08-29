from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/hello2')
def hello2():
    names = [{"name":"xxx"},{"name":"yyy"}]
    return render_template('hello2.html', names=names)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)


