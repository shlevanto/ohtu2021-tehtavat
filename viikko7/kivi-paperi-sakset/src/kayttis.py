from enum import Enum
from kps import KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly


class Kayttis:
    def __init__(self):
        self._komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

    def _suorita_komento(self, komento):
        komento.pelaa()

    def kaynnista(self):
        while True:
            print(
                    "Valitse pelataanko"
                    "\n (a) Ihmistä vastaan"
                    "\n (b) Tekoälyä vastaan"
                    "\n (c) Parannettua tekoälyä vastaan"
                    "\nMuilla valinnoilla lopetetaan"
                )

            vastaus = input()

            if vastaus in "abc":
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                self._suorita_komento(self._komennot[vastaus])

            else:
                break

