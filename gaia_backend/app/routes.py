# app/routes.py
from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})