import json
import unittest
from flask import Flask
from unittest.mock import patch
from src.httpApi import send_http_error, send_http_response

class TestHttpApiFunctions(unittest.TestCase):

    def setUp(self):
        # Create a Flask app and set it to testing mode
        self.app = Flask(__name__)
        self.app.testing = True

    @patch('httpApi.jsonify')
    def test_send_http_error(self, mock_jsonify):
        error_message = "Test error message"
        status_code = 404

        # Configure the mock 'jsonify' function to return a mock JSON response
        mock_response = {'error': error_message, 'status_code': status_code}
        mock_jsonify.return_value = mock_response

        # Call the send_http_error function
        with self.app.app_context():
            response, code = send_http_error(error_message, status_code)
            
             # Transform the response into a JSON object
            response_json = response.json

        # Check if the status code matches the expected status code
        print("#### Send HTTP error #### Test status : Check if the status code matches the expected status code.")
        self.assertEqual(code, status_code)

        # Check if the response JSON is as expected
        print("#### Send HTTP error #### Test status : Check if the response JSON is as expected.")
        self.assertEqual(response_json, mock_response)

    @patch('httpApi.jsonify')
    def test_send_http_response(self, mock_jsonify):
        test_response = "Test response message"

        # Configure the mock 'jsonify' function to return a mock JSON response
        mock_response = {'response': test_response, 'status_code': 200}
        mock_jsonify.return_value = mock_response

        # Call the send_http_response function
        with self.app.app_context():
            response, code = send_http_response(test_response)

            # Transform the response into a JSON object
            response_json = response.json

        # Check if the status code is 200 (OK)
        print("#### Send HTTP response #### Test status : Check if the status code is 200 (OK).")
        self.assertEqual(code, 200)

        # Check if the response JSON is as expected
        print("#### Send HTTP response #### Test status : Check if the response JSON is as expected.")
        self.assertEqual(response_json, mock_response)

if __name__ == '__main__':
    unittest.main()
