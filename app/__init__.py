from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.routes import video_services_vw

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)

    CORS(app, resources={
        r"/api/*": {  # Aplica CORS solo a rutas que comienzan con /api/
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],  # REMPLAZAR POR PUERTO DE CONSULTA DE FLUTTER XD
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
        }
    })

    app.register_blueprint(video_services_vw.bp, url_prefix="/api/video_services")  # Ajustar URL base del blueprint

    return app
