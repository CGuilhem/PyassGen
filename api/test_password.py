import unittest
import string
# from api import app  
from password import generate_password
from password import hash_password  # Replace 'your_password_module' with the actual module name

class TestPasswordHashing(unittest.TestCase):

    def test_hash_password(self):
        # Test hashing a password
        password = "my_secure_password"
        hashed_password = hash_password(password)

        # Check if the hashed password is not equal to the plain-text password
        print("#### Hash #### Test status : Check if the hashed password is not equal to the plain-text password.")
        self.assertNotEqual(hashed_password, password)

        # Test hashing the same password again (should produce different hashes)
        rehashed_password = hash_password(password)

        # Check if the rehashed password is not equal to the plain-text password
        print("#### Hash #### Test status : Check if the rehashed password is not equal to the plain-text password.")
        self.assertNotEqual(rehashed_password, password)

        # Check if the rehashed password is not equal to the original hashed password
        print("#### Hash #### Test status : Check if the rehashed password is not equal to the original hashed password.")
        self.assertNotEqual(rehashed_password, hashed_password)

class TestPasswordFunction(unittest.TestCase):

    def test_generate_password(self):

        # Test with a password length of 8 characters, including numbers and symbols
        password = generate_password(8, 1, 1)
        
        # Check if the generated password meets the length requirement
        print("#### Generate password #### Test status : Check if the generated password meets the length requirement. (8)")
        self.assertEqual(len(password), 8)

        # Test with a password length of 25 characters, including numbers and symbols
        password = generate_password(25, 1, 1)
        
        # Check if the generated password meets the length requirement
        print("#### Generate password #### Test status : Check if the generated password meets the length requirement. (25)")
        self.assertEqual(len(password), 25)

        # Test with a password length of 100 characters, including numbers and symbols
        password = generate_password(100, 1, 1)
        
        # Check if the generated password meets the length requirement
        print("#### Generate password #### Test status : Check if the generated password meets the length requirement. (100)")
        self.assertEqual(len(password), 100)

        # Test with an invalid password length (0 characters)
        password_lensIs0 = generate_password(0, include_numbers=True, include_symbols=True)
        print("#### Generate password #### Test status : Test with an invalid password length (0 characters).")
        self.assertEqual(password_lensIs0, None)

        # Test with an invalid password length (negative number of characters)
        password_Negative = generate_password(-5, include_numbers=True, include_symbols=True)
        print("#### Generate password #### Test status : Test with an invalid password length (negative number of characters).")
        self.assertEqual(password_Negative, None)
        
if __name__ == '__main__':
    unittest.main()
