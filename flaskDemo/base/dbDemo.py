import pymysql
from flask import Flask, session, render_template, request, redirect, url_for, g, flash
import logging
import collections


app = Flask(__name__)
app.config.from_object('config')


@app.before_request
def before_request():
    conn = pymysql.connect(host=app.config['MYSQL_HOST'],
                           port=3306,
                           user=app.config['MYSQL_USER'],
                           passwd=app.config['MYSQL_PASSWORD'],
                           db=app.config['MYSQL_DBNAME'],
                           charset='utf8')
    g.conn = conn
    g.cursor = conn.cursor()


@app.teardown_request
def teardown_request(exception):
    logging.info(exception)
    conn = g.conn
    cursor = g.cursor
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        passwd = request.form['passwd']
        cursor = g.cursor
        cursor.execute("select count(id) from users where name=%s and password=%s ", (name, passwd))
        query = cursor.fetchone()
        if query[0] == 1:
            session['user'] = name
            flash('Login successfully!', 'message')
            if name == 'admin':
                cursor.execute("select * from users")
                rows = cursor.fetchall()
                accounts = []
                for row in rows:
                    account = collections.OrderedDict()
                    account['id'] = row[0]
                    account['name'] = row[1]
                    account['passwd'] = row[2]
                    accounts.append(account)
                return render_template('admin.html', accounts=accounts)
            return redirect(url_for('index'))
        else:
            flash('No such user!', 'error')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/')
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['user']
        passwd = request.form['passwd']
        cursor = g.cursor
        cursor.execute("insert into users(name, password) values(%s, %s)", (name, passwd))
        g.conn.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route('/index')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('login'), 302)


if __name__ == '__main__':
    app.run(host="127.0.0.1", post=8080)