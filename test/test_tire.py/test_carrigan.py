import unittest

from tire.carrigan import Carrigan

class TestCarriganTire(unittest.TestCase):

    def value_true(self):
        res = [1,0.5,0.3,0.7]

        tire = Carrigan(res)  

        self.assertTrue(tire)
    
    def value_false(self):
        res = [0.1,0.5,0.3,0.7]

        tire = Carrigan(res)

        self.assertFalse(tire)

        