from flask import Flask
from flask import render_template, redirect, url_for, request
import sys
import os

app = Flask(__name__)


# Route for handling the Index
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('login.html')


# Route for handling the login page logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    print(request.form)
    if request.method == 'POST':
        _user = request.form['user']
        _pass =  request.form['pass']
        _cpass = request.form['c-pass']
        _email = request.form['email']
        print(_user, _pass, _cpass)
        if _user and _pass:
            if _pass==_cpass:
                return render_template('post-registering.html', to=_user)
            else:
                return render_template('login.html', error='Password Mismatch')
        else:
            return render_remplate('login.html', error='Missing fields') 
    else:
        return render_template('login.html')  



# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        _user = request.form['user']
        _pass =  request.form['pass']
        if _user and _pass:
            return render_template('post-login.html', to=request.form['user'])
        else:
            return render_template('login.html', error='Missing Fields')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4005, debug =True)