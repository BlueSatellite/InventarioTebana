from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Cliente

bp = Blueprint('clientes', __name__, url_prefix='/clientes')


@bp.route('/')
def lista():
    clientes = Cliente.query.order_by(Cliente.nombre).all()
    return render_template('clientes/lista.html', clientes=clientes)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form.get('contacto', '')
        tipo = request.form.get('tipo', '')
        direccion = request.form.get('direccion', '')
        notas = request.form.get('notas', '')

        cliente = Cliente(
            nombre=nombre,
            contacto=contacto,
            tipo=tipo,
            direccion=direccion,
            notas=notas
        )
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente creado.', 'success')
        return redirect(url_for('clientes.lista'))

    return render_template('clientes/nuevo.html')


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.contacto = request.form.get('contacto', '')
        cliente.tipo = request.form.get('tipo', '')
        cliente.direccion = request.form.get('direccion', '')
        cliente.notas = request.form.get('notas', '')
        db.session.commit()
        flash('Cliente actualizado.', 'success')
        return redirect(url_for('clientes.lista'))

    return render_template('clientes/editar.html', cliente=cliente)


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente eliminado.', 'success')
    return redirect(url_for('clientes.lista'))
