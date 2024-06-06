from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')


from model import Sucursal, Repartidor, Paquete, Transporte, db

@app.route('/')
def index():
    if not session.get('name'):
        return redirect('/login')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['nombre']
        return redirect('/')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
