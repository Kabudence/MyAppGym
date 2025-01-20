from flask import jsonify, Blueprint
from sqlalchemy import text

from app import db

bp = Blueprint('video_services', __name__)

@bp.route('/info', methods=['GET'])
def get_video_services_view():
    query = db.session.execute(text("SELECT * FROM vw_servicios_videos;")).mappings()
    resultados = [dict(row) for row in query]
    return jsonify(resultados), 200
