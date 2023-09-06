import binascii
import os
import random
import string
import hashlib
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

def hash_password(password):
    # Create a salt (a random value) to add to the password before hashing
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # Add the salt to the password and hash the result
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Convert the binary hash to a hexadecimal representation
    password_hash = binascii.hexlify(password_hash)
    # Combine the salt and hashed password as a single string
    hashed_password = (salt + password_hash).decode('ascii')
    return hashed_password