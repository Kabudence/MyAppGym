from flask import jsonify, Blueprint
from sqlalchemy import text

from app import db

bp = Blueprint('video_services', __name__)

@bp.route('/info', methods=['GET'])
def get_video_services_view():
    query = db.session.execute(text("SELECT * FROM vw_servicios_videos;")).mappings()
    resultados = [dict(row) for row in query]
    return jsonify(resultados), 200

# CREATE VIEW vw_servicios_videos AS
# SELECT
#     servicios.ID AS servicio_id,
#     servicios.nombre AS servicio_nombre,
#     videos_settings.sesión AS video_sesion,
#     videos_settings.descripcion AS video_descripcion,
#     videos_settings.video AS video_url
# FROM
#     servicios
# JOIN
#     videos_settings ON videos_settings.id = servicios.ID;
