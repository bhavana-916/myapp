# tests/test_app.py
import unittest
from app import app

class FlaskCalculatorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', json={'a': 5, 'b': 3, 'operation': 'add'})
        self.assertEqual(response.json['result'], 8)

    def test_subtraction(self):
        response = self.app.post('/calculate', json={'a': 10, 'b': 4, 'operation': 'subtract'})
        self.assertEqual(response.json['result'], 6)

    def test_multiplication(self):
        response = self.app.post('/calculate', json={'a': 2, 'b': 3, 'operation': 'multiply'})
        self.assertEqual(response.json['result'], 6)

    def test_division(self):
        response = self.app.post('/calculate', json={'a': 9, 'b': 3, 'operation': 'divide'})
        self.assertEqual(response.json['result'], 3)

    def test_division_by_zero(self):
        response = self.app.post('/calculate', json={'a': 5, 'b': 0, 'operation': 'divide'})
        self.assertEqual(response.json['error'], 'Division by zero is not allowed')

if __name__ == '__main__':
    unittest.main()
