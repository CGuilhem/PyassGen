import unittest
import string
from password import generate_password  # Make sure to adjust the import to match your file structure

class TestGeneratePassword(unittest.TestCase):

    def test_generate_password(self):
        # Test with a password length of 8 characters, including numbers and symbols
        password = generate_password(8, include_numbers=True, include_symbols=True)
        self.assertEqual(len(password), 8)  # Check length
        self.assertTrue(any(c.isdigit() for c in password))  # Check for the presence of digits
        self.assertTrue(any(c in string.punctuation for c in password))  # Check for the presence of symbols

        # Test with a password length of 12 characters, without numbers or symbols
        password = generate_password(12, include_numbers=False, include_symbols=False)
        self.assertEqual(len(password), 12)  # Check length
        self.assertFalse(any(c.isdigit() for c in password))  # Check for the absence of digits
        self.assertFalse(any(c in string.punctuation for c in password))  # Check for the absence of symbols

        # Test with an invalid password length (0 characters)
        with self.assertRaises(ValueError):
            generate_password(0, include_numbers=True, include_symbols=True)

if __name__ == '__main__':
    unittest.main()
