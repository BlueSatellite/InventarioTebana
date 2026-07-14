from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Receta, RecetaInsumo, Ingrediente
from app.calculators import calcular_ibu, calcular_abv, calcular_srm_morey, kg_a_lbs, litros_a_galones

bp = Blueprint('recetas', __name__, url_prefix='/recetas')


@bp.route('/')
def lista():
    recetas = Receta.query.order_by(Receta.created_at.desc()).all()
    return render_template('recetas/lista.html', recetas=recetas)


@bp.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        nombre = request.form['nombre']
        estilo = request.form.get('estilo', '')
        volumen = float(request.form.get('volumen_objetivo_l', 20))
        eficiencia = float(request.form.get('eficiencia', 70))
        og = float(request.form.get('og_objetivo', 1.050) or 1.050)
        fg = float(request.form.get('fg_objetivo', 1.012) or 1.012)
        notas = request.form.get('notas', '')

        receta = Receta(
            nombre=nombre,
            estilo=estilo,
            volumen_objetivo_l=volumen,
            eficiencia=eficiencia,
            og_objetivo=og,
            fg_objetivo=fg,
            notas=notas
        )

        color_total = 0
        ibu_total = 0
        volumen_l = volumen
        volumen_gal = litros_a_galones(volumen)

        tipos = request.form.getlist('insumo_tipo[]')
        ing_ids = request.form.getlist('insumo_ingrediente_id[]')
        cantidades = request.form.getlist('insumo_cantidad[]')
        unidades = request.form.getlist('insumo_unidad[]')
        tiempos = request.form.getlist('insumo_tiempo[]')
        usos = request.form.getlist('insumo_uso[]')

        for i, tipo in enumerate(tipos):
            if i >= len(ing_ids) or not ing_ids[i]:
                continue
            ingrediente = Ingrediente.query.get(int(ing_ids[i]))
            if not ingrediente:
                continue
            cantidad = float(cantidades[i]) if i < len(cantidades) and cantidades[i] else 0
            unidad = unidades[i] if i < len(unidades) else 'kg'
            tiempo = int(tiempos[i]) if i < len(tiempos) and tiempos[i] else 0
            uso = usos[i] if i < len(usos) else ''

            insumo = RecetaInsumo(
                receta=receta,
                ingrediente_id=ingrediente.id,
                cantidad=cantidad,
                unidad=unidad,
                tiempo=tiempo,
                uso=uso
            )
            db.session.add(insumo)

            if tipo == 'malta' and ingrediente.lovibond > 0:
                peso_lbs = kg_a_lbs(cantidad) if unidad == 'kg' else cantidad
                srm = calcular_srm_morey(ingrediente.lovibond, peso_lbs, volumen_gal)
                color_total += srm

            if tipo == 'lupulo' and ingrediente.alpha_acido > 0 and tiempo > 0:
                ibu = calcular_ibu(ingrediente.alpha_acido, cantidad * 1000, volumen_l, og, tiempo)
                ibu_total += ibu

        receta.ibu_objetivo = round(ibu_total, 1)
        receta.color_objetivo = round(color_total, 1)

        db.session.add(receta)
        db.session.commit()
        flash('Receta creada correctamente.', 'success')
        return redirect(url_for('recetas.ver', id=receta.id))

    ingredientes = Ingrediente.query.order_by(Ingrediente.tipo, Ingrediente.nombre).all()
    return render_template('recetas/nueva.html', ingredientes=ingredientes)


@bp.route('/<int:id>')
def ver(id):
    receta = Receta.query.get_or_404(id)
    volumen_gal = litros_a_galones(receta.volumen_objetivo_l)
    volumen_l = receta.volumen_objetivo_l

    insumos_con_calculos = []
    ibu_total = 0
    color_total = 0
    og = receta.og_objetivo or 1.050

    porcentajes = {}
    peso_total_malta = 0
    for insumo in receta.insumos:
        if insumo.ingrediente.tipo == 'malta':
            peso = insumo.cantidad if insumo.unidad == 'kg' else insumo.cantidad
            peso_total_malta += peso

    for insumo in receta.insumos:
        ing = insumo.ingrediente
        info = {
            'insumo': insumo,
            'ingrediente': ing,
            'ibu': 0,
            'srm': 0,
            'porcentaje': 0
        }
        if ing.tipo == 'malta':
            peso_lbs = kg_a_lbs(insumo.cantidad) if insumo.unidad == 'kg' else insumo.cantidad
            srm = calcular_srm_morey(ing.lovibond, peso_lbs, volumen_gal)
            info['srm'] = srm
            color_total += srm
            if peso_total_malta > 0:
                peso = insumo.cantidad if insumo.unidad == 'kg' else insumo.cantidad
                info['porcentaje'] = round((peso / peso_total_malta) * 100, 1)
        if ing.tipo == 'lupulo':
            ibu = calcular_ibu(ing.alpha_acido or 0, insumo.cantidad * 1000, volumen_l, og, insumo.tiempo or 0)
            info['ibu'] = ibu
            ibu_total += ibu

        insumos_con_calculos.append(info)

    abv_estimado = calcular_abv(receta.og_objetivo, receta.fg_objetivo)

    return render_template('recetas/ver.html',
                           receta=receta,
                           insumos_con_calculos=insumos_con_calculos,
                           ibu_total=round(ibu_total, 1),
                           color_total=round(color_total, 1),
                           abv_estimado=abv_estimado)


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    receta = Receta.query.get_or_404(id)

    if request.method == 'POST':
        receta.nombre = request.form['nombre']
        receta.estilo = request.form.get('estilo', '')
        receta.volumen_objetivo_l = float(request.form.get('volumen_objetivo_l', 20))
        receta.eficiencia = float(request.form.get('eficiencia', 70))
        receta.og_objetivo = float(request.form.get('og_objetivo', 1.050) or 1.050)
        receta.fg_objetivo = float(request.form.get('fg_objetivo', 1.012) or 1.012)
        receta.notas = request.form.get('notas', '')

        RecetaInsumo.query.filter_by(receta_id=receta.id).delete()

        volumen_l = receta.volumen_objetivo_l
        volumen_gal = litros_a_galones(volumen_l)
        color_total = 0
        ibu_total = 0
        og = receta.og_objetivo

        tipos = request.form.getlist('insumo_tipo[]')
        ing_ids = request.form.getlist('insumo_ingrediente_id[]')
        cantidades = request.form.getlist('insumo_cantidad[]')
        unidades = request.form.getlist('insumo_unidad[]')
        tiempos = request.form.getlist('insumo_tiempo[]')
        usos = request.form.getlist('insumo_uso[]')

        for i, tipo in enumerate(tipos):
            if i >= len(ing_ids) or not ing_ids[i]:
                continue
            ingrediente = Ingrediente.query.get(int(ing_ids[i]))
            if not ingrediente:
                continue
            cantidad = float(cantidades[i]) if i < len(cantidades) and cantidades[i] else 0
            unidad = unidades[i] if i < len(unidades) else 'kg'
            tiempo = int(tiempos[i]) if i < len(tiempos) and tiempos[i] else 0
            uso = usos[i] if i < len(usos) else ''

            insumo = RecetaInsumo(
                receta_id=receta.id,
                ingrediente_id=ingrediente.id,
                cantidad=cantidad,
                unidad=unidad,
                tiempo=tiempo,
                uso=uso
            )
            db.session.add(insumo)

            if tipo == 'malta' and ingrediente.lovibond > 0:
                peso_lbs = kg_a_lbs(cantidad) if unidad == 'kg' else cantidad
                srm = calcular_srm_morey(ingrediente.lovibond, peso_lbs, volumen_gal)
                color_total += srm

            if tipo == 'lupulo' and ingrediente.alpha_acido > 0 and tiempo > 0:
                ibu = calcular_ibu(ingrediente.alpha_acido, cantidad * 1000, volumen_l, og, tiempo)
                ibu_total += ibu

        receta.ibu_objetivo = round(ibu_total, 1)
        receta.color_objetivo = round(color_total, 1)

        db.session.commit()
        flash('Receta actualizada correctamente.', 'success')
        return redirect(url_for('recetas.ver', id=receta.id))

    ingredientes = Ingrediente.query.order_by(Ingrediente.tipo, Ingrediente.nombre).all()
    return render_template('recetas/editar.html', receta=receta, ingredientes=ingredientes)


@bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    receta = Receta.query.get_or_404(id)
    db.session.delete(receta)
    db.session.commit()
    flash('Receta eliminada.', 'success')
    return redirect(url_for('recetas.lista'))
