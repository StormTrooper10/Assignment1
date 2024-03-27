import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_route(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World')

    def test_calc_add_route(self):
        response = self.app.get('/calc/add/2/3')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 5)

    def test_calc_subtract_route(self):
        response = self.app.get('/calc/subtract/5/3')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2)

    def test_calc_multiply_route(self):
        response = self.app.get('/calc/multiply/2/3')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 6)

    def test_invalid_operation(self):
        response = self.app.get('/calc/divide/2/3')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['error'], 'Invalid operation. Please use add, subtract, or multiply.')

if __name__ == '__main__':
    unittest.main()
