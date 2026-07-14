from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Ingrediente

bp = Blueprint('inventario', __name__, url_prefix='/inventario')

TIPOS = ['malta', 'lupulo', 'levadura', 'adjunto', 'otro']


@bp.route('/')
def lista():
    tipo_filtro = request.args.get('tipo', '')
    alerta = request.args.get('alerta', '')

    query = Ingrediente.query

    if tipo_filtro:
        query = query.filter_by(tipo=tipo_filtro)

    if alerta == 'minimo':
        query = query.filter(Ingrediente.stock_minimo > 0,
                             Ingrediente.cantidad <= Ingrediente.stock_minimo)

    ingredientes = query.order_by(Ingrediente.tipo, Ingrediente.nombre).all()
    return render_template('inventario/lista.html', ingredientes=ingredientes, tipos=TIPOS,
                           tipo_filtro=tipo_filtro, alerta=alerta, hoy=date.today())


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        cantidad = float(request.form.get('cantidad', 0))
        unidad = request.form.get('unidad', 'kg')
        stock_minimo = float(request.form.get('stock_minimo', 0))
        precio = float(request.form.get('precio', 0))
        lote = request.form.get('lote_interno', '')
        caducidad = request.form.get('fecha_caducidad', '')
        notas = request.form.get('notas', '')
        alpha = float(request.form.get('alpha_acido', 0))
        lovibond = float(request.form.get('lovibond', 0))

        from datetime import datetime
        fecha = datetime.strptime(caducidad, '%Y-%m-%d').date() if caducidad else None

        ing = Ingrediente(
            nombre=nombre,
            tipo=tipo,
            cantidad=cantidad,
            unidad=unidad,
            stock_minimo=stock_minimo,
            precio=precio,
            lote_interno=lote,
            fecha_caducidad=fecha,
            notas=notas,
            alpha_acido=alpha,
            lovibond=lovibond
        )
        db.session.add(ing)
        db.session.commit()
        flash('Ingrediente agregado al inventario.', 'success')
        return redirect(url_for('inventario.lista'))

    return render_template('inventario/nuevo.html', tipos=TIPOS)


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    ing = Ingrediente.query.get_or_404(id)

    if request.method == 'POST':
        ing.nombre = request.form['nombre']
        ing.tipo = request.form['tipo']
        ing.cantidad = float(request.form.get('cantidad', 0))
        ing.unidad = request.form.get('unidad', 'kg')
        ing.stock_minimo = float(request.form.get('stock_minimo', 0))
        ing.precio = float(request.form.get('precio', 0))
        ing.lote_interno = request.form.get('lote_interno', '')
        ing.notas = request.form.get('notas', '')
        ing.alpha_acido = float(request.form.get('alpha_acido', 0))
        ing.lovibond = float(request.form.get('lovibond', 0))

        caducidad = request.form.get('fecha_caducidad', '')
        from datetime import datetime
        ing.fecha_caducidad = datetime.strptime(caducidad, '%Y-%m-%d').date() if caducidad else None

        db.session.commit()
        flash('Ingrediente actualizado.', 'success')
        return redirect(url_for('inventario.lista'))

    return render_template('inventario/editar.html', ingrediente=ing, tipos=TIPOS)


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    ing = Ingrediente.query.get_or_404(id)
    db.session.delete(ing)
    db.session.commit()
    flash('Ingrediente eliminado.', 'success')
    return redirect(url_for('inventario.lista'))


@bp.route('/<int:id>/ajustar-stock', methods=['POST'])
def ajustar_stock(id):
    ing = Ingrediente.query.get_or_404(id)
    operacion = request.form.get('operacion', 'sumar')
    cantidad = float(request.form.get('cantidad', 0))

    if operacion == 'sumar':
        ing.cantidad += cantidad
    elif operacion == 'restar':
        ing.cantidad = max(0, ing.cantidad - cantidad)
    elif operacion == 'fijar':
        ing.cantidad = cantidad

    db.session.commit()
    flash(f'Stock de {ing.nombre} actualizado.', 'success')
    return redirect(url_for('inventario.lista'))
