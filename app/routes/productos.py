from flask import Blueprint, jsonify
from app.models import Product

bp = Blueprint('productos', __name__)

@bp.route('/products', methods=['GET'])
def get_all_products():
    """
    Endpoint para obtener todos los productos con campos resumidos.
    """
    products = Product.query.all()
    return jsonify([product.to_summary_dict() for product in products])

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint para obtener un producto por su ID con todos los campos.
    """
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(product.to_full_dict())
