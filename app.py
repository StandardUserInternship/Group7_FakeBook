from flask import Flask, render_template
from flask import request, redirect, url_for   


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"


@app.route('/welcome')
def welcome():
    return render_template('Welcome.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Try again Pal'
        else:
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)

