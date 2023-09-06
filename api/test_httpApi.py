import unittest
from api import app
from httpApi import send_http_error, send_http_response

class TestFlaskFunctions(unittest.TestCase):

    def test_send_http_error(self):
        # Create a test Flask app context
        with app.test_request_context():
            error_message = "Test error message"
            status_code = 404

            response, code = send_http_error(error_message, status_code)

            # Check if the response JSON contains the error message and status code
            self.assertEqual(code, status_code)
            self.assertEqual(response.json['error'], error_message)

    def test_send_http_response(self):
        # Create a test Flask app context
        with app.test_request_context():
            test_response = "Test response message"

            response, code = send_http_response(test_response)

            # Check if the response JSON contains the response message and status code
            self.assertEqual(code, 200)
            self.assertEqual(response.json['response'], test_response)

if __name__ == '__main__':
    unittest.main()
