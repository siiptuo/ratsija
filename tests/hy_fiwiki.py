import unittest
from ratsija import hy_fiwiki

class TestTransliterate(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(hy_fiwiki('Երևան'), 'Jerevan')

    def test_example2(self):
        self.assertEqual(hy_fiwiki('Լևոն Հակոբի Տեր-Պետրոսյան'), 'Levon Hakobi Ter-Petrosjan')

    def test_example3(self):
        self.assertEqual(hy_fiwiki('Ռոբերտ Սեդրակի Քոչարյան'), 'Robert Sedraki Kotšarjan')

    def test_example4(self):
        self.assertEqual(hy_fiwiki('Սերժ Ազատի Սարգսյան'), 'Serž Azati Sargsjan')

    def test_example5(self):
        self.assertEqual(hy_fiwiki('Արմեն Վարդանի Սարգսյան'), 'Armen Vardani Sargsjan')

    def test_example6(self):
        self.assertEqual(hy_fiwiki('Ալեն Ռոբերտի Սիմոնյան'), 'Alen Roberti Simonjan')

    def test_example7(self):
        self.assertEqual(hy_fiwiki('Վահագն Գառնիկի Խաչատուրյան'), 'Vahagn Garniki Khatšaturjan')

if __name__ == '__main__':
    unittest.main()
