from flask import Blueprint, render_template
from app.models import Receta, Lote, Ingrediente, Barril, Pedido

bp = Blueprint('dashboard', __name__, url_prefix='/')


@bp.route('/')
def index():
    total_recetas = Receta.query.count()
    total_lotes = Lote.query.count()
    lotes_activos = Lote.query.filter(Lote.estado.in_(['planificado', 'coccion', 'fermentando', 'madurando'])).count()
    lotes_listos = Lote.query.filter_by(estado='listo').count()

    alertas_stock = Ingrediente.query.filter(
        Ingrediente.stock_minimo > 0,
        Ingrediente.cantidad <= Ingrediente.stock_minimo
    ).all()

    barriles_prestados = Barril.query.filter(Barril.cliente_id != None).all()

    lotes_recientes = Lote.query.order_by(Lote.created_at.desc()).limit(5).all()
    pedidos_pendientes = Pedido.query.filter_by(estado='pendiente').count()

    return render_template('index.html',
                           total_recetas=total_recetas,
                           total_lotes=total_lotes,
                           lotes_activos=lotes_activos,
                           lotes_listos=lotes_listos,
                           alertas_stock=alertas_stock,
                           barriles_prestados=barriles_prestados,
                           lotes_recientes=lotes_recientes,
                           pedidos_pendientes=pedidos_pendientes)
