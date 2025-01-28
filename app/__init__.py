from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Inicializar la base de datos
    db.init_app(app)

    # Configuración de CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
        }
    })

    # Importar blueprints después de inicializar app
    with app.app_context():
        from app.routes import video_services_vw, productos, mis_favoritos
        app.register_blueprint(video_services_vw.bp, url_prefix="/api/video_services")
        app.register_blueprint(productos.bp, url_prefix="/api/productos")
        app.register_blueprint(mis_favoritos.bp, url_prefix="/api/mis_favoritos")

    return app
