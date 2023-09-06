from flask import Flask
from flask_cors import CORS
from httpApi import send_http_response, send_http_error
from password import generate_password

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Welcome to PYassGen!</p>"

@app.route("/password/<int:length>/<include_numbers>/<include_symbols>")
def send_password(length, include_numbers, include_symbols):
    password = generate_password(length, include_numbers, include_symbols)

    if (password == None):
      return send_http_error("La longueur du mot de passe doit être supérieure à zéro.", 400)
    else:
      response = {
          'password': password
      }
      return send_http_response(response)