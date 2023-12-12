import json
import os
import subprocess
import sys

from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_bcrypt import Bcrypt
import secrets
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

# Configure SSL
ssl_context = ('cert.crt', 'private.key')

if not os.path.isfile(ssl_context[0]) or not os.path.isfile(ssl_context[1]):
    openssl_command = [
        "openssl",
        "req",
        "-x509",
        "-newkey", "rsa:4096",
        "-nodes",
        "-out", ssl_context[0],
        "-keyout", ssl_context[1],
        "-subj", "/CN=localhost",
    ]

    result = subprocess.run(openssl_command, capture_output=True, text=True)
    print(result)

pw = secrets.token_urlsafe(12)
root_pw = secrets.token_urlsafe(16)
print("pw: ", pw)
print("root pw: ", root_pw)
users = {
    'skywalker': {'username': 'skywalker', 'password': bcrypt.generate_password_hash(pw).decode('utf-8')},
    'skywalker_goes_root': {'username': 'skywalker_goes_root', 'password': bcrypt.generate_password_hash(root_pw).decode('utf-8')},
}


def get_user(username):
    return users.get(username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(username)

        if user and bcrypt.check_password_hash(user['password'], password):
            flash('Login successful!', 'success')
            session[username] = username
            # Here you can redirect to a secure area or perform other actions
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')


@app.route('/')
def home():
    if any(key in session for key in ['skywalker', 'skywalker_goes_root']):
        return render_template('index.html')

    return redirect(url_for('login'))


@app.route('/process_data', methods=['POST'])
def process_data():
    import methods
    data = request.form['input_data']
    if len(data) > 2:
        res = methods.get_cmd_output(data)
    else:
        res = None

    return json.dumps(res)


if __name__ == '__main__':
    host = sys.argv[1]
    app.run(debug=True, port=8000, host=host, ssl_context=ssl_context)
