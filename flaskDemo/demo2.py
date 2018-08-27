from flask import Flask, Markup


app = Flask(__name__)


@app.route('/')
def hello():
    return '<div>Hello %s</div>' % '<em>Flask</em>'
    # return Markup('<div>Hello %s </div>') % '<em>Flask</em>' #防注入


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)