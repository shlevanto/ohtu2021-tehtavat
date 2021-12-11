import kps


class Kayttis:
    def kaynnista(self):
        while True:
            print("Valitse pelataanko"
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

            if vastaus.endswith("a"):
                kaksinpeli = kps.KPSPelaajaVsPelaaja()
                kaksinpeli.pelaa()

            elif vastaus.endswith("b"):
                yksinpeli = kps.KPSTekoaly()
                yksinpeli.pelaa()

            elif vastaus.endswith("c"):
                haastava_yksinpeli = kps.KPSParempiTekoaly()
                haastava_yksinpeli.pelaa()

            else:
                break
