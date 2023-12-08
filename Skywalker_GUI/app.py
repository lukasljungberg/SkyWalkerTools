
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_bcrypt import Bcrypt
import secrets
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

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
    data = request.form['input_data']
    # Do something with the data (e.g., print it)
    print(f"Received data: {data}")
    return 'Data received successfully!'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
