from flask import Flask
from flask_cors import CORS, cross_origin
from httpApi import send_http_response, send_http_error
from password import generate_password, hash_password

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<p>Welcome to PYassGen!</p>"

@app.route("/password/<int:length>/<include_numbers>/<include_symbols>/<include_hash>")
def send_password(length, include_numbers, include_symbols, include_hash):
      
    password = generate_password(length, include_numbers, include_symbols)

    if (password == None):
      return send_http_error("La longueur du mot de passe doit être supérieure à zéro.", 400)
    else:
      hashed_password = hash_password(password) if include_hash == '1' else ""
      response = {
          'password': password,
          'hash': hashed_password
      }
      return send_http_response(response)