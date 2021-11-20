from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.korin_ostokset = []
        
    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

        return sum([o.lukumaara() for o in self.korin_ostokset])
        
    def hinta(self):
        return sum([o.hinta() for o in self.korin_ostokset])
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        nimet = [o.tuotteen_nimi() for o in self.korin_ostokset]
        
        if lisattava.nimi() in nimet:
            [o.muuta_lukumaaraa(1) for o in self.korin_ostokset if o.tuotteen_nimi() == lisattava.nimi()]
        else:
            self.korin_ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        [o.muuta_lukumaaraa(-1) for o in self.korin_ostokset if o.tuotteen_nimi() == poistettava.nimi()]
        # poistaa listalta tuotteet, joiden lukumäärä on 0
        self.korin_ostokset = [o for o in self.korin_ostokset if o.lukumaara() > 0]

    def tyhjenna(self):
        self.korin_ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.korin_ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
