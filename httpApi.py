from flask import jsonify

def send_http_error(error, status_code):
    response = {
        'error': error,
        'status_code': status_code
    }
    return jsonify(response), status_code

def send_http_response(response):
    response = {
        'response': response,
        'status_code': 200
    }
    return jsonify(response), 200