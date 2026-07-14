import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "cerveceria.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'cerveceria-secreta-2024')

    os.makedirs(basedir, exist_ok=True)

    db.init_app(app)

    from app.routes import dashboard, recetas, inventario, lotes, ventas, clientes, barriles
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(recetas.bp)
    app.register_blueprint(inventario.bp)
    app.register_blueprint(lotes.bp)
    app.register_blueprint(ventas.bp)
    app.register_blueprint(clientes.bp)
    app.register_blueprint(barriles.bp)

    with app.app_context():
        from app import models
        db.create_all()

    return app
