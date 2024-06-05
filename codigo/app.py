from flask import Flask, render_template, request, redirect,session
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login', methods=['POST', 'GET'])
def bienvenida():
    if request.method == 'POST':
        if request.form['nombre'] and request.form['email'] and request.form['password']:
            datosf=request.form
            return render_template('login.html', datos=datosf, hora=datetime.now().hour)
        else:
            return render_template('login.html', error='Invalid username or password')

if __name__ == '__main__':
    app.run(debug=True)     

