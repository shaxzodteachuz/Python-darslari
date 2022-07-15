import unittest

from numpy import unsignedinteger
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchuun test"""
    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
    def test_create(self):
        # Qiymatlar mavjudligini assertNotNone metodi bilan aniqlaymiz.
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.aseertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIstNone metodi bilan aniqlaymiz.
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan aniqlaymiz. 
        self.assertEqual(0,self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price,self.avto2.price)

unittest.main()
