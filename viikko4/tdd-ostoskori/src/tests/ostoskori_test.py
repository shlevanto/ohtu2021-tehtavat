import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_tavara(self):
        bisse = Tuote('Bisse', 3)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        bisse = Tuote('Bisse', 3)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        bisse = Tuote('Bisse', 3)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
