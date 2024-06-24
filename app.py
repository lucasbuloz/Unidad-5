from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config.from_pyfile('config.py')
from model import db, Sucursal, Paquete, Transporte 


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    role = request.form.get('role')
    if role == 'despachante':
        return redirect(url_for('funcion1'))
    elif role == 'repartidor':
        return render_template('repartidor.html')

@app.route('/repartidor')
def repartidor():
    return render_template('index.html')

@app.route("/funcion1")
def funcion1():
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('funcion1.html', sucursales=sucursales)

@app.route("/funcion2", methods=['GET', 'POST'])
def funcion2():
    if request.method == 'POST':
        print(request.form)
        idsucursal = request.form.get('idsucursal')
        peso = request.form.get('peso')
        dirdestinatario = request.form.get('dirdestinatario')
        nomdestinatario = request.form.get('nomdestinatario')
        if not nomdestinatario:
            flash("El nombre del destinatario es obligatorio", "error")
            return redirect(url_for('funcion2'))
        entregado = request.form.get('entregado') == '1' 
        observaciones = request.form.get('observaciones')
        numeroenvio = random.randint(1000, 1500)
        idtransporte = request.form.get('idTransporte')
        idrepartidor = request.form.get('idRepartidor')
        paquete = Paquete(numeroenvio=numeroenvio, peso=peso, nomdestinatario=nomdestinatario, dirdestinatario=dirdestinatario, entregado=entregado, observaciones=observaciones, idsucursal=idsucursal, idtransporte=idtransporte, idrepartidor=idrepartidor)
        db.session.add(paquete)
        db.session.commit()
        flash("Paquete registrado con éxito", "success")
        return redirect(url_for('funcion1'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.id).all()
        return render_template('funcion2.html', sucursales=sucursales)


    
@app.route("/funcion3", methods=['GET', 'POST'])
def funcion3():
    if request.method == 'POST':
        paquete_ids = request.form.getlist('paquetes')
        id_sucursal = request.form.get('id_sucursal')
        if not paquete_ids:
            flash("No se han seleccionado paquetes para el transporte", "error")
            return redirect(url_for('funcion3', sucursal=id_sucursal))
        
        try:
           
            transporte = Transporte(
                numerotransporte=random.randint(1000, 1500),
                fechahorasalida=datetime.now(),
                fechahorallegada=None,
                idsucursal=id_sucursal
            )
            db.session.add(transporte)
            db.session.commit()
            
            
            for paquete_id in paquete_ids:
                paquete = Paquete.query.get(paquete_id)
                paquete.idtransporte = transporte.id
                db.session.commit()
            
            flash("Transporte registrado con éxito", "success")
        except Exception as e:
            db.session.rollback()
            flash("Error al registrar el transporte", "error")
        
        return redirect(url_for('funcion1'))
    else:
        id_sucursal = request.args.get('sucursal')
        if not id_sucursal:
            return redirect(url_for('funcion1'))
        
        paquetes = Paquete.query.filter_by(entregado=0, idrepartidor=0).all()
        return render_template('funcion3.html', paquetes=paquetes, id_sucursal=id_sucursal)

    
    
@app.route("/funcion4", methods=['GET', 'POST'])
def funcion4():
    if request.method == 'POST':
        try:
            transporte_id = request.form.get('transporte_id')
            transporte = Transporte.query.get(transporte_id)
            if transporte and not transporte.fechahorallegada:
                transporte.fechahorallegada = datetime.now()
                db.session.commit()
                flash("Llegada del transporte registrada con éxito", "success")
            else:
                flash("Transporte no válido o ya registrado", "error")
        except Exception as e:
            db.session.rollback()
            flash("Error al registrar llegada del transporte", "error")
        return redirect(url_for('funcion1'))
    
    elif request.method == 'GET':
        sucursal_id = request.args.get('sucursal')
        if not sucursal_id:
            flash("No se ha especificado la sucursal", "error")
            return redirect(url_for('funcion1'))

        transportes = Transporte.query.filter_by(idsucursal=sucursal_id, fechahorallegada=None).all()
        
        if not transportes:
            flash("No hay transportes pendientes de llegada", "error")
        
        return render_template('funcion4.html', transportes=transportes)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)