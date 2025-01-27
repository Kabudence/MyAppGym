from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer)
    description = db.Column(db.Text)
    marca = db.Column(db.String(100))
    link_video_one = db.Column(db.String(100))
    link_video_two = db.Column(db.String(100))
    purchase_price = db.Column(db.Numeric(10, 2))
    price = db.Column(db.Numeric(10, 2))
    descuento = db.Column(db.Numeric(10, 2))
    previous_price = db.Column(db.Numeric(10, 2))
    date = db.Column(db.Date)
    sort = db.Column(db.Integer)
    image_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    weight = db.Column(db.String(100))
    longs = db.Column(db.String(100))
    long_sleeve = db.Column(db.String(100))
    back_width = db.Column(db.String(100))
    breast_contour = db.Column(db.String(100))
    waist = db.Column(db.String(100))
    hip = db.Column(db.String(100))
    status = db.Column(db.Integer)
    relevant = db.Column(db.Integer)
    additional = db.Column(db.String(200))
    brand = db.Column(db.String(100))
    qty = db.Column(db.Integer)
    outstanding = db.Column(db.Integer)
    fotos_talla = db.Column(db.Text)
    palabras_claves = db.Column(db.Text)
    tipo_producto = db.Column(db.Integer)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    promocion = db.Column(db.Integer)
    id_product_size = db.Column(db.Integer)
    horario = db.Column(db.String(150))
    horario_foto = db.Column(db.String(100))
    profesor = db.Column(db.String(100))
    profesor_foto = db.Column(db.String(100))

    def __repr__(self):
        return f"<Product {self.title}>"

    def to_summary_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_name": self.image_name,
            "price": float(self.price) if self.price else None,
            "previous_price": float(self.previous_price) if self.previous_price else None,
            "discount": float(self.descuento) if self.descuento else None,
            "brand": self.marca,
            "video_links": [
                link for link in [self.link_video_one, self.link_video_two] if link
            ]
        }

    def to_full_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
