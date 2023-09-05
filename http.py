from flask import jsonify

def sendHttpError(error, statusCode):
    response = {
        'error': error,
        'status_code': statusCode
    }
    return jsonify(response), statusCode

def sendHttpResponse(response):
    return jsonify(response)