from flask import Blueprint, jsonify
from . import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/cases')
def get_cases():
    return jsonify({"status": "success", "data": []})
