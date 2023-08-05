import unittest

from tire.octoprime import Octoprime

class TestOctoprimeTire(unittest.TestCase):

    def value_true(self):
        res = [1,0.9,0.6,0.7]

        tire = Octoprime(res)  

        self.assertTrue(tire)
    
    def value_false(self):
        res = [0.1,0.5,0.3,0.7]

        tire = Octoprime(res)

        self.assertFalse(tire)