from flask import Flask, session, redirect, request, render_template, url_for,make_response
import time


app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H-%M-%S'), 3600)
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            return render_template('login.html', title=title)
    return response


app.secret_key = '9999999'


if __name__ == '__main__':
    app.run()