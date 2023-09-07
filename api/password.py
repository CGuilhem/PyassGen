import binascii
import os
import random
import string
import hashlib

def generate_password(length, include_numbers, include_symbols):
    characters = string.ascii_letters  # Lettres majuscules et minuscules par défaut

    if length < 1:
        return None
    
    if (include_numbers == '1'):
        characters += string.digits  # Ajoutez des chiffres

    if (include_symbols == '1'):
        characters += string.punctuation  # Ajoutez des symboles
    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def hash_password(password, is_salted):
    # Create a salt (a random value) to add to the password before hashing
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # Add the salt to the password and hash the result
    if(is_salted):
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    else:
         password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 100000)
    # Convert the binary hash to a hexadecimal representation
    password_hash = binascii.hexlify(password_hash)
    # Combine the salt and hashed password as a single string
    hashed_password = (salt + password_hash).decode('ascii')
    return hashed_password

def evaluate_password(password):
    # Initial score is 0
    score = 0

    # Check the length of the password
    if len(password) >= 8:
        score += 2  # Award 2 points for a sufficient length

    # Check if the password includes numbers
    if any(c.isdigit() for c in password):
        score += 2  # Award 2 points for including numbers

    # Check if the password includes uppercase letters
    if any(c.isupper() for c in password):
        score += 2  # Award 2 points for including uppercase letters

    # Check if the password includes special characters
    if any(c in string.punctuation for c in password):
        score += 2  # Award 2 points for including special characters

    # Define rating categories based on the score
    if score >= 8:
        rating = "Fort"
    elif score >= 4:
        rating = "Moyen"
    else:
        rating = "Faible"

    return rating

if __name__ == '__main__':
    password = generate_password(12, True, True)
    print("Mot de passe généré :", password)
    rating = evaluate_password(password)
    print("Qualité du mot de passe :", rating)
