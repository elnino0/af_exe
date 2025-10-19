from http import HTTPStatus
from flask import Blueprint, request,jsonify
from app.services.ScanMockSerivce import ScanMockSerivce
bp = Blueprint('scan', __name__, url_prefix='/scan')


scanMockService = ScanMockSerivce()
@bp.route('/', methods=['POST'])
def scan():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"success": False, "message": "No token provided"}), HTTPStatus.UNAUTHORIZED
    return scanMockService.scanFile(request.files)