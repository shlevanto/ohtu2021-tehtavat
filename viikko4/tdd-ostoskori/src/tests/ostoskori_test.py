import unittest
from ostoskori import Ostoskori
from tuote import Tuote

bisse = Tuote('Bisse', 3)
sipsit = Tuote('Sipsit', 2)


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_tavara(self):
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hintaon_kahden_tuotteen_hinta(self):
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        
        self.assertEqual(self.kori.hinta(), 6)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(bisse)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(bisse)
        
        ostos = self.kori.ostokset()[0]
        
        self.assertAlmostEqual(ostos.tuotteen_nimi(), 'Bisse')
        self.assertAlmostEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(sipsit)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 2)