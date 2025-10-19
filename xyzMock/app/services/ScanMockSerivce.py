from http import HTTPStatus # Good practice for returning standard HTTP codes
import hashlib
from werkzeug.utils import secure_filename
from flask import jsonify

class ScanMockSerivce:
    def __init__(self):
        pass

    def scanFile(self, files):
        if 'file' not in files:
            return jsonify({
                    "success": False, 
                    "message": "Missing file key in request (expected 'file')."
            }), HTTPStatus.BAD_REQUEST

        file = files['file']
        if file.filename == '':
                return jsonify({
                    "success": False, 
                    "message": "No file selected."
                }), HTTPStatus.BAD_REQUEST 
        filename = secure_filename(file.filename)
        return jsonify({
                    "file_hash:": hashlib.sha256(filename.encode()).hexdigest(),
                    "threat_found": "low"
                }), HTTPStatus.OK 
