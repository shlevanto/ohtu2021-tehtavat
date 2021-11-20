import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.bisse = Tuote('Bisse', 3)
        
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_tavara(self):
        self.kori.lisaa_tuote(self.bisse)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.bisse)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.bisse)
        self.kori.lisaa_tuote(self.bisse)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hintaon_kahden_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.bisse)
        self.kori.lisaa_tuote(self.bisse)
        
        self.assertEqual(self.kori.hinta(), 6)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.bisse)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)
