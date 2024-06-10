from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')


from model import Sucursal, Repartidor, Paquete, Transporte, db

@app.route('/')
def index():
    return render_template('funcion1.html')



@app.route("/funcion1")
def funcion1():
    if request.method == 'POST':
        session['name'] = request.form['nombre']
        return redirect('/funcion1')
    return render_template('funcion1.html')

@app.route("/sucursal2", methods=['GET', 'POST'])
def sucursal2():
    if not session.get('name'):
        return redirect('/funcion1')
    return render_template('sucursal2.html')

@app.route("/sucursal3", methods=['GET', 'POST'])
def sucursal3():
    if not session.get('name'):
        return redirect('/funcion1')
    return render_template('sucursal3.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
