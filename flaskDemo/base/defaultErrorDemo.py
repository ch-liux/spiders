from flask import Flask, make_response, redirect, url_for
from logging.handlers import TimedRotatingFileHandler
import logging

app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response


@app.route('/login')
def login():
    app.logger.debug('error debug')
    app.logger.error('error error')
    #”server.log”记录所有级别日志；”error.log”只记录错误日志
    server_log = TimedRotatingFileHandler('server.log', 'D')
    server_log.setLevel(logging.DEBUG)
    server_log.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

    error_log = TimedRotatingFileHandler('server.log', 'D')
    error_log.setLevel(logging.ERROR)
    error_log.setFormatter(logging.Formatter('%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d])'))

    app.logger.addHandler(server_log)
    app.logger.addHandler(error_log)

    raise InvalidUsage("ERROR")


@app.route('/')
def index():
    # 默认为302；301，303，305，307
    return redirect(url_for('login'), 302)


if __name__ == "__main__":
    app.run()