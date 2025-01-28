from app import db

class MisFavoritos(db.Model):
    __tablename__ = 'MisFavoritos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sesion = db.Column(db.String(250), nullable=False)
    video = db.Column(db.String(350), nullable=False)
    descripcion = db.Column(db.String(500), nullable=True)
    id_servicio = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    estado = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'sesion': self.sesion,
            'video': self.video,
            'descripcion': self.descripcion,
            'id_servicio': self.id_servicio,
            'user_id': self.user_id,
            'estado': self.estado
        }