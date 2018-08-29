from flask import request, session
from flask import render_template
from flask import Flask
from flask import redirect, url_for


app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    print(request.form)
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s !' % session['user']
    else:
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.secret_key = '123456'


if __name__ == '__main__':
    app.run()