from datetime import date, datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Lote, Receta, RecetaInsumo, RegistroFermentacion, Ingrediente

bp = Blueprint('lotes', __name__, url_prefix='/lotes')

ESTADOS = ['planificado', 'coccion', 'fermentando', 'madurando', 'listo', 'envasado', 'vendido']


@bp.route('/')
def lista():
    estado_filtro = request.args.get('estado', '')
    query = Lote.query
    if estado_filtro:
        query = query.filter_by(estado=estado_filtro)
    lotes = query.order_by(Lote.created_at.desc()).all()
    return render_template('lotes/lista.html', lotes=lotes, estados=ESTADOS, estado_filtro=estado_filtro)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        receta_id = int(request.form.get('receta_id', 0) or 0)
        volumen = float(request.form.get('volumen_objetivo_l', 20))
        notas = request.form.get('notas', '')

        receta = Receta.query.get(receta_id) if receta_id else None

        lote = Lote(
            nombre=nombre,
            receta_id=receta_id if receta_id else 1,
            estado='planificado',
            fecha_inicio=date.today(),
            volumen_objetivo_l=volumen,
            notas=notas
        )
        db.session.add(lote)
        db.session.commit()

        if receta:
            for insumo in receta.insumos:
                ing = insumo.ingrediente
                if ing:
                    ing.cantidad = max(0, ing.cantidad - insumo.cantidad)
            db.session.commit()

        flash('Lote creado y stock descontado.', 'success')
        return redirect(url_for('lotes.ver', id=lote.id))

    recetas = Receta.query.order_by(Receta.nombre).all()
    return render_template('lotes/nuevo.html', recetas=recetas)


@bp.route('/<int:id>')
def ver(id):
    lote = Lote.query.get_or_404(id)
    registros = RegistroFermentacion.query.filter_by(lote_id=id).order_by(RegistroFermentacion.fecha.asc()).all()
    return render_template('lotes/ver.html', lote=lote, registros=registros, estados=ESTADOS)


@bp.route('/<int:id>/actualizar-estado', methods=['POST'])
def actualizar_estado(id):
    lote = Lote.query.get_or_404(id)
    nuevo_estado = request.form.get('estado', '')
    if nuevo_estado in ESTADOS:
        lote.estado = nuevo_estado
        if nuevo_estado in ('listo', 'envasado', 'vendido'):
            lote.fecha_fin = date.today()
        db.session.commit()
        flash(f'Estado actualizado a: {nuevo_estado}', 'success')
    return redirect(url_for('lotes.ver', id=id))


@bp.route('/<int:id>/agregar-registro', methods=['POST'])
def agregar_registro(id):
    lote = Lote.query.get_or_404(id)
    temp = float(request.form.get('temperatura', 0))
    grav = float(request.form.get('gravedad', 0))
    notas = request.form.get('notas', '')

    registro = RegistroFermentacion(
        lote_id=id,
        fecha=datetime.utcnow(),
        temperatura=temp,
        gravedad=grav,
        notas=notas
    )
    db.session.add(registro)

    if grav > 0 and lote.og_real is None:
        lote.og_real = grav
    if grav > 0 and lote.estado == 'fermentando':
        lote.fg_real = grav

    db.session.commit()
    flash('Registro de fermentacion agregado.', 'success')
    return redirect(url_for('lotes.ver', id=id))
