from flask import abort, Flask, render_template

app = Flask(__name__)


@app.route('/error')
def error():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()