from flask import Flask, session, request, make_response, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'login in successfully!'
        else:
            return 'login in fial!'
    if 'user' in session:
        return "hello %s " % session['user']
    else:
        title = request.args.get('title', 'Default')
        response = make_response(render_template('login.html', title=title), 200)
        # 自定义头部 
        response.headers['key'] = 'value'
        return response


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.secret_key = '123456'


if __name__ == "__main__":
    app.run()