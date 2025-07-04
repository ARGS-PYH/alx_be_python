import unittest
from simple_calculator import SimpleCalculator

class TestSimple_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    
    def test_addition(self):
        self.assertEqual(self.calc.add(4,2),6)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,4),8)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2),2)
        
        
    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5,0),)    
    
        
   
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()