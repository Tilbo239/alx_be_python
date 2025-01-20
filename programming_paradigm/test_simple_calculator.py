import unittest
from  simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):

        self.assertEqual(self.calc.add(4, 3), 7)
        self.assertEqual(self.calc.add(-15, 1), -14)
        self.assertEqual(self.calc.add(-3,-1),-4)
        self.assertEqual(self.calc.add(-11,11),0 )
    
    def test_subtraction(self):

        self.assertEqual(self.calc.subtract(2, 34), -32)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(1,-1), 2)
    
    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(1,-1), -1)
    
    def test_division(self):

        self.assertEqual(self.calc.divide(20, 2), 10.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-1, 1), -1.0)
        self.assertEqual(self.calc.divide(-2,-2), 1.0)
        self.assertEqual(self.calc.divide(0,10), 0.0)
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)