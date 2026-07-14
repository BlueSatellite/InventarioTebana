from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Cliente, Pedido, LineaPedido, Barril

bp = Blueprint('ventas', __name__, url_prefix='/ventas')


@bp.route('/')
def lista():
    pedidos = Pedido.query.order_by(Pedido.fecha.desc()).all()
    return render_template('ventas/lista.html', pedidos=pedidos)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        cliente_id = int(request.form.get('cliente_id', 0))
        notas = request.form.get('notas', '')

        pedido = Pedido(
            cliente_id=cliente_id,
            fecha=date.today(),
            estado='pendiente',
            total=0,
            notas=notas
        )
        db.session.add(pedido)
        db.session.flush()

        total = 0
        productos = request.form.getlist('producto[]')
        cantidades = request.form.getlist('cantidad[]')
        precios = request.form.getlist('precio_unitario[]')
        lote_ids = request.form.getlist('lote_id[]')

        for i, producto in enumerate(productos):
            if not producto:
                continue
            cantidad = float(cantidades[i]) if i < len(cantidades) else 1
            precio = float(precios[i]) if i < len(precios) else 0
            lote_id = int(lote_ids[i]) if i < len(lote_ids) and lote_ids[i] else None
            total += cantidad * precio

            linea = LineaPedido(
                pedido_id=pedido.id,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio,
                lote_id=lote_id
            )
            db.session.add(linea)

        pedido.total = total
        db.session.commit()
        flash('Pedido creado.', 'success')
        return redirect(url_for('ventas.lista'))

    clientes = Cliente.query.order_by(Cliente.nombre).all()
    return render_template('ventas/nuevo.html', clientes=clientes)


@bp.route('/<int:id>')
def ver(id):
    pedido = Pedido.query.get_or_404(id)
    return render_template('ventas/ver.html', pedido=pedido)


@bp.route('/<int:id>/actualizar-estado', methods=['POST'])
def actualizar_estado(id):
    pedido = Pedido.query.get_or_404(id)
    estado = request.form.get('estado', '')
    if estado in ('pendiente', 'entregado', 'pagado', 'cancelado'):
        pedido.estado = estado
        db.session.commit()
        flash(f'Estado del pedido actualizado a: {estado}', 'success')
    return redirect(url_for('ventas.ver', id=id))


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido eliminado.', 'success')
    return redirect(url_for('ventas.lista'))
