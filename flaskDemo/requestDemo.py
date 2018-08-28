from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)