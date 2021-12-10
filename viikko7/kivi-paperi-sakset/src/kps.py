from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print("Kiitos!")
            print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmaisen pelaajan siirto: ")

    def _toisen_siirto(self, siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto in "kps"


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, siirto):
        return input("Toisen pelaajan siirto: ")


class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, siirto):
        seuraava_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {seuraava_siirto}")

        return seuraava_siirto


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
