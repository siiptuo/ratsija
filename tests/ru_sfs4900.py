import unittest
from ratsija import ru_sfs4900

class TestTransliterate(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(ru_sfs4900('Анапа'), 'Anapa')

    def test_example2(self):
        self.assertEqual(ru_sfs4900('Бабаево'), 'Babajevo')

    def test_example3(self):
        self.assertEqual(ru_sfs4900('Всеволожск'), 'Vsevoložsk')

    def test_example4(self):
        self.assertEqual(ru_sfs4900('Гагарин'), 'Gagarin')

    def test_example5(self):
        self.assertEqual(ru_sfs4900('Дедовск'), 'Dedovsk')

    def test_example6(self):
        self.assertEqual(ru_sfs4900('Дальнереченск'), 'Dalneretšensk')

    def test_example7(self):
        self.assertEqual(ru_sfs4900('Егорьевск'), 'Jegorjevsk')

    def test_example8(self):
        self.assertEqual(ru_sfs4900('Гаджиево'), 'Gadžijevo')

    def test_example9(self):
        self.assertEqual(ru_sfs4900('Горбачёв'), 'Gorbatšov')

    def test_example10(self):
        self.assertEqual(ru_sfs4900('Тимашёвск'), 'Timašovsk')

    def test_example11(self):
        self.assertEqual(ru_sfs4900('Хрущёв'), 'Hruštšov')

    def test_example12(self):
        self.assertEqual(ru_sfs4900('Королёв'), 'Koroljov')

    def test_example13(self):
        self.assertEqual(ru_sfs4900('Железнодорожный'), 'Železnodorožnyi')

    def test_example14(self):
        self.assertEqual(ru_sfs4900('Заозёрск'), 'Zaozjorsk')

    def test_example15(self):
        self.assertEqual(ru_sfs4900('Ишим'), 'Išim')

    def test_example16(self):
        self.assertEqual(ru_sfs4900('Краснотурьинск'), 'Krasnoturjinsk')

    def test_example17(self):
        self.assertEqual(ru_sfs4900('Ясный'), 'Jasnyi')

    def test_example18(self):
        self.assertEqual(ru_sfs4900('Валдайский район'), 'Valdaiski raion')

    def test_example19(self):
        self.assertEqual(ru_sfs4900('Каспийск'), 'Kaspijsk')

    def test_example20(self):
        self.assertEqual(ru_sfs4900('Йошкар-Ола'), 'Joškar-Ola')

    def test_example21(self):
        self.assertEqual(ru_sfs4900('Чайковский'), 'Tšaikovski')

    def test_example22(self):
        self.assertEqual(ru_sfs4900('Копейск'), 'Kopeisk')

    def test_example23(self):
        self.assertEqual(ru_sfs4900('Лихославль'), 'Lihoslavl')

    def test_example24(self):
        self.assertEqual(ru_sfs4900('Мурманск'), 'Murmansk')

    def test_example25(self):
        self.assertEqual(ru_sfs4900('Ногинск'), 'Noginsk')

    def test_example26(self):
        self.assertEqual(ru_sfs4900('Олонец'), 'Olonets')

    def test_example27(self):
        self.assertEqual(ru_sfs4900('Почеп'), 'Potšep')

    def test_example28(self):
        self.assertEqual(ru_sfs4900('Рязань'), 'Rjazan')

    def test_example29(self):
        self.assertEqual(ru_sfs4900('Сестрорецк'), 'Sestroretsk')

    def test_example30(self):
        self.assertEqual(ru_sfs4900('Тольятти'), 'Toljatti')

    def test_example31(self):
        self.assertEqual(ru_sfs4900('Уссурийск'), 'Ussurijsk')

    def test_example32(self):
        self.assertEqual(ru_sfs4900('Фатеж'), 'Fatež')

    def test_example33(self):
        self.assertEqual(ru_sfs4900('Хабаровск'), 'Habarovsk')

    def test_example34(self):
        self.assertEqual(ru_sfs4900('Цивильск'), 'Tsivilsk')

    def test_example35(self):
        self.assertEqual(ru_sfs4900('Чита'), 'Tšita')

    def test_example36(self):
        self.assertEqual(ru_sfs4900('Шушары'), 'Šušary')

    def test_example37(self):
        self.assertEqual(ru_sfs4900('Щёлково'), 'Štšolkovo')

    def test_example38(self):
        self.assertEqual(ru_sfs4900('субъект'), 'subjekt')

    def test_example39(self):
        self.assertEqual(ru_sfs4900('Кызыл'), 'Kyzyl')

    def test_example40(self):
        self.assertEqual(ru_sfs4900('Козьмодемьянск'), 'Kozmodemjansk')

    def test_example41(self):
        self.assertEqual(ru_sfs4900('Энгельс'), 'Engels')

    def test_example42(self):
        self.assertEqual(ru_sfs4900('Юрюзань'), 'Jurjuzan')

    def test_example43(self):
        self.assertEqual(ru_sfs4900('Ярославль'), 'Jaroslavl')

if __name__ == '__main__':
    unittest.main()
