import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('Shaxzodjon','Zoirov')
# assertEqual- testlarni tekshirish uchun ishlatiladigan method hisoblanadi.        
        self.assertEqual(name, 'Shaxzodjon Zoirov')

    def test_otasining_ismi(self):
        name = get_full_name('Shaxzodjon','Zoirov','Po"latovich')
        self.assertEqual(name,'Shaxzodjon Po"latovich Zoirov')

unittest.main()