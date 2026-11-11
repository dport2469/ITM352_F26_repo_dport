# make a simple flask app that starts a web server 
from flask import Flask, redirect, render_template, request, url_for

my_name = "Dan"
USERS = {"port": "port123", "kazman": "kazman123"}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', my_name=my_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if USERS.get(username) == password:
            return redirect(url_for('success'))
        return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=5000)