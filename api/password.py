import random
import string
from httpApi import send_http_error, send_http_response

def generate_password(length, include_numbers, include_symbols):
    characters = string.ascii_letters  # Lettres majuscules et minuscules par défaut

    if length < 1:
        return None
    
    if include_numbers:
        characters += string.digits  # Ajoutez des chiffres

    if include_symbols:
        characters += string.punctuation  # Ajoutez des symboles

    password = ''.join(random.choice(characters) for _ in range(length))

    return password
