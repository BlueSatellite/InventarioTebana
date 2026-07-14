from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Barril, Cliente

bp = Blueprint('barriles', __name__, url_prefix='/barriles')


@bp.route('/')
def lista():
    barriles = Barril.query.order_by(Barril.nombre).all()
    clientes = Cliente.query.order_by(Cliente.nombre).all()
    disponibles = sum(1 for b in barriles if b.estado == 'disponible')
    sucios = sum(1 for b in barriles if b.estado == 'sucio')
    prestados = sum(1 for b in barriles if b.estado == 'prestado')
    return render_template('barriles/lista.html',
                           barriles=barriles, clientes=clientes,
                           disponibles=disponibles, sucios=sucios, prestados=prestados)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        capacidad = float(request.form.get('capacidad_l', 20))
        contenido = request.form.get('contenido_actual', '')
        ubicacion = request.form.get('ubicacion', '')
        estado = request.form.get('estado', 'disponible')

        barril = Barril(
            nombre=nombre,
            capacidad_l=capacidad,
            contenido_actual=contenido,
            ubicacion=ubicacion,
            estado=estado
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
        barril.fecha_devolucion = None
        barril.estado = 'prestado'
        flash(f'Barril prestado a {barril.cliente.nombre}.', 'success')
    db.session.commit()
    return redirect(url_for('barriles.lista'))


@bp.route('/<int:id>/devolver', methods=['POST'])
def devolver(id):
    barril = Barril.query.get_or_404(id)
    barril.cliente_id = None
    barril.fecha_devolucion = date.today()
    barril.estado = 'sucio'
    barril.contenido_actual = ''
    flash('Barril devuelto (marcado como sucio).', 'success')
    db.session.commit()
    return redirect(url_for('barriles.lista'))


@bp.route('/<int:id>/limpiar', methods=['POST'])
def limpiar(id):
    barril = Barril.query.get_or_404(id)
    barril.estado = 'disponible'
    barril.contenido_actual = ''
    flash('Barril limpio y disponible.', 'success')
    db.session.commit()
    return redirect(url_for('barriles.lista'))


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    barril = Barril.query.get_or_404(id)
    if request.method == 'POST':
        barril.nombre = request.form['nombre']
        barril.capacidad_l = float(request.form.get('capacidad_l', 20))
        barril.contenido_actual = request.form.get('contenido_actual', '')
        barril.ubicacion = request.form.get('ubicacion', '')
        barril.estado = request.form.get('estado', barril.estado)
        cliente_id = int(request.form.get('cliente_id', 0) or 0)
        if cliente_id and barril.estado == 'prestado':
            barril.cliente_id = cliente_id
            if not barril.fecha_prestamo:
                barril.fecha_prestamo = date.today()
        elif barril.estado != 'prestado':
            barril.cliente_id = None
        db.session.commit()
        flash('Barril actualizado.', 'success')
        return redirect(url_for('barriles.lista'))

    clientes = Cliente.query.order_by(Cliente.nombre).all()
    return render_template('barriles/editar.html', barril=barril, clientes=clientes)


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    barril = Barril.query.get_or_404(id)
    db.session.delete(barril)
    db.session.commit()
    flash('Barril eliminado.', 'success')
    return redirect(url_for('barriles.lista'))
