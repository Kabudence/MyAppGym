from flask import Blueprint, jsonify, request
from app import db
from app.models.misfavoritos import MisFavoritos

bp = Blueprint('mis_favoritos', __name__)

@bp.route('/misfavoritos', methods=['GET'])
def get_all_favorites():
    """
    Endpoint para obtener todos los favoritos con campos resumidos.
    """
    favoritos = MisFavoritos.query.all()
    return jsonify([favorito.to_dict() for favorito in favoritos])

@bp.route('/misfavoritos/<int:favorito_id>', methods=['GET'])
def get_favorite_by_id(favorito_id):
    """
    Endpoint para obtener un favorito por su ID con todos los campos.
    """
    favorito = MisFavoritos.query.get(favorito_id)
    if not favorito:
        return jsonify({"error": "Favorito no encontrado"}), 404
    return jsonify(favorito.to_dict())

@bp.route('/misfavoritos', methods=['POST'])
def create_favorite():
    """
    Endpoint para crear un nuevo favorito.
    """
    data = request.json
    try:
        nuevo_favorito = MisFavoritos(
            sesion=data['sesion'],
            video=data['video'],
            descripcion=data.get('descripcion'),
            id_servicio=data['id_servicio'],
            user_id=data['user_id'],
            estado=data.get('estado', True)
        )
        db.session.add(nuevo_favorito)
        db.session.commit()
        return jsonify(nuevo_favorito.to_dict()), 201
    except KeyError as e:
        return jsonify({"error": f"Campo requerido faltante: {str(e)}"}), 400

@bp.route('/misfavoritos/<int:favorito_id>', methods=['PUT'])
def update_favorite(favorito_id):
    """
    Endpoint para actualizar un favorito existente.
    """
    favorito = MisFavoritos.query.get(favorito_id)
    if not favorito:
        return jsonify({"error": "Favorito no encontrado"}), 404

    data = request.json
    favorito.sesion = data.get('sesion', favorito.sesion)
    favorito.video = data.get('video', favorito.video)
    favorito.descripcion = data.get('descripcion', favorito.descripcion)
    favorito.id_servicio = data.get('id_servicio', favorito.id_servicio)
    favorito.user_id = data.get('user_id', favorito.user_id)
    favorito.estado = data.get('estado', favorito.estado)

    db.session.commit()
    return jsonify(favorito.to_dict())

@bp.route('/misfavoritos/<int:favorito_id>', methods=['DELETE'])
def delete_favorite(favorito_id):
    """
    Endpoint para eliminar un favorito por su ID.
    """
    favorito = MisFavoritos.query.get(favorito_id)
    if not favorito:
        return jsonify({"error": "Favorito no encontrado"}), 404

    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"message": "Favorito eliminado correctamente"}), 200
