from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Barril, Cliente

bp = Blueprint('barriles', __name__, url_prefix='/barriles')


@bp.route('/')
def lista():
    barriles = Barril.query.order_by(Barril.nombre).all()
    clientes = Cliente.query.order_by(Cliente.nombre).all()
    return render_template('barriles/lista.html', barriles=barriles, clientes=clientes)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        capacidad = float(request.form.get('capacidad_l', 20))
        contenido = request.form.get('contenido_actual', '')
        ubicacion = request.form.get('ubicacion', '')

        barril = Barril(
            nombre=nombre,
            capacidad_l=capacidad,
            contenido_actual=contenido,
            ubicacion=ubicacion
        )
        db.session.add(barril)
        db.session.commit()
        flash('Barril agregado.', 'success')
        return redirect(url_for('barriles.lista'))

    return render_template('barriles/nuevo.html')


@bp.route('/<int:id>/prestar', methods=['POST'])
def prestar(id):
    barril = Barril.query.get_or_404(id)
    cliente_id = int(request.form.get('cliente_id', 0))
    if cliente_id:
        barril.cliente_id = cliente_id
        barril.fecha_prestamo = date.today()
        barril.ubicacion = None
    else:
        barril.cliente_id = None
        barril.fecha_prestamo = None
        barril.ubicacion = request.form.get('ubicacion', '')
    db.session.commit()
    flash('Barril actualizado.', 'success')
    return redirect(url_for('barriles.lista'))


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    barril = Barril.query.get_or_404(id)
    db.session.delete(barril)
    db.session.commit()
    flash('Barril eliminado.', 'success')
    return redirect(url_for('barriles.lista'))
