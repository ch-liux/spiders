from flask import render_template, request, session, url_for, redirect, flash, Flask


app = Flask(__name__)


@app.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('login'), 302)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        # ”message”, “info”, “warning”, “error”
        flash('Login successfully!', 'message')
        flash('Login as user: %s.' % request.form['user'], 'info')
        return redirect(url_for('index'))
    else:
        return """
            <form name="login" action="/login" method="post">
                Username: <input type="text" name="user" />
            </form>
        """


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('login'))


app.secret_key = '12580'


if __name__ == '__main__':
    app.run()