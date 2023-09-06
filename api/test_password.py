# import unittest
# import string
# from api import app  
# from password import generate_password

# class TestPasswordFunction(unittest.TestCase):

#     def test_generate_password(self):
#         # Create a test Flask app context
#         with app.test_request_context():
#             # Test with a password length of 8 characters, including numbers and symbols
#             password = generate_password(8, 1, 1)
            
#             # Check if the generated password meets the length requirement
#             self.assertEqual(len(password), 8)

#             # If numbers and symbols are included, check if they are present in the password
#             if password:
#                 self.assertTrue(any(c.isdigit() for c in password))  # Check for the presence of digits
#                 self.assertTrue(any(c in string.punctuation for c in password))  # Check for the presence of symbols

#         # Test with an invalid password length (0 characters)
#         with self.assertRaises(ValueError):
#             generate_password(0, include_numbers=True, include_symbols=True)

# if __name__ == '__main__':
#     unittest.main()
