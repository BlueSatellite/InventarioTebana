from datetime import datetime, date
from app import db


class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # malta, lupulo, levadura, adjunto, otro
    cantidad = db.Column(db.Float, default=0)
    unidad = db.Column(db.String(10), default='kg')
    stock_minimo = db.Column(db.Float, default=0)
    precio = db.Column(db.Float, default=0)
    lote_interno = db.Column(db.String(50))
    fecha_caducidad = db.Column(db.Date)
    notas = db.Column(db.Text)
    alpha_acido = db.Column(db.Float, default=0)
    lovibond = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Receta(db.Model):
    __tablename__ = 'recetas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    estilo = db.Column(db.String(50))
    volumen_objetivo_l = db.Column(db.Float, default=20)
    eficiencia = db.Column(db.Float, default=70)
    og_objetivo = db.Column(db.Float)
    fg_objetivo = db.Column(db.Float)
    ibu_objetivo = db.Column(db.Float)
    color_objetivo = db.Column(db.Float)
    notas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    insumos = db.relationship('RecetaInsumo', backref='receta', lazy=True, cascade='all, delete-orphan')
    lotes = db.relationship('Lote', backref='receta', lazy=True)


class RecetaInsumo(db.Model):
    __tablename__ = 'receta_insumos'

    id = db.Column(db.Integer, primary_key=True)
    receta_id = db.Column(db.Integer, db.ForeignKey('recetas.id'), nullable=False)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    cantidad = db.Column(db.Float, default=0)
    unidad = db.Column(db.String(10), default='kg')
    tiempo = db.Column(db.Integer, default=0)  # minutos en hervor (para lúpulos)
    uso = db.Column(db.String(20))  # amargor, sabor, aroma (para lúpulos)

    ingrediente = db.relationship('Ingrediente')


class Lote(db.Model):
    __tablename__ = 'lotes'

    id = db.Column(db.Integer, primary_key=True)
    receta_id = db.Column(db.Integer, db.ForeignKey('recetas.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(30), default='planificado')
    # planificado, coccion, fermentando, madurando, listo, envasado, vendido
    fecha_inicio = db.Column(db.Date, default=date.today)
    fecha_fin = db.Column(db.Date)
    volumen_objetivo_l = db.Column(db.Float)
    volumen_real_l = db.Column(db.Float)
    og_real = db.Column(db.Float)
    fg_real = db.Column(db.Float)
    ibu_real = db.Column(db.Float)
    color_real = db.Column(db.Float)
    notas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    registros = db.relationship('RegistroFermentacion', backref='lote', lazy=True, cascade='all, delete-orphan')


class RegistroFermentacion(db.Model):
    __tablename__ = 'registros_fermentacion'

    id = db.Column(db.Integer, primary_key=True)
    lote_id = db.Column(db.Integer, db.ForeignKey('lotes.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    temperatura = db.Column(db.Float)
    gravedad = db.Column(db.Float)
    notas = db.Column(db.Text)


class Barril(db.Model):
    __tablename__ = 'barriles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    capacidad_l = db.Column(db.Float, default=20)
    contenido_actual = db.Column(db.String(100))
    ubicacion = db.Column(db.String(100))
    estado = db.Column(db.String(20), default='disponible')  # disponible, sucio, prestado
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha_prestamo = db.Column(db.Date)
    fecha_devolucion = db.Column(db.Date)

    cliente = db.relationship('Cliente', foreign_keys=[cliente_id])


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100))
    tipo = db.Column(db.String(30))  # bar, restaurante, retail, particular
    direccion = db.Column(db.String(200))
    notas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)
    barriles = db.relationship('Barril', backref='cliente_prestatario', lazy=True, foreign_keys=[Barril.cliente_id])


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    fecha = db.Column(db.Date, default=date.today)
    estado = db.Column(db.String(30), default='pendiente')  # pendiente, entregado, pagado, cancelado
    total = db.Column(db.Float, default=0)
    notas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    lineas = db.relationship('LineaPedido', backref='pedido', lazy=True, cascade='all, delete-orphan')


class LineaPedido(db.Model):
    __tablename__ = 'lineas_pedido'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Float, default=1)
    precio_unitario = db.Column(db.Float, default=0)
    lote_id = db.Column(db.Integer, db.ForeignKey('lotes.id'))
