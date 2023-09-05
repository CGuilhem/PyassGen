import random
import string
from http import sendHttpError, sendHttpResponse

def generatePassword(length, include_numbers=True, include_symbols=True):
    characters = string.ascii_letters  # Lettres majuscules et minuscules par défaut

    if include_numbers:
        characters += string.digits  # Ajoutez des chiffres

    if include_symbols:
        characters += string.punctuation  # Ajoutez des symboles

    if length < 1:
        sendHttpError("La longueur du mot de passe doit être supérieure à zéro.", 400)

    password = ''.join(random.choice(characters) for _ in range(length))
    response = {
        'password': password,
        'status_code': 200
    }
    sendHttpResponse(response) 

