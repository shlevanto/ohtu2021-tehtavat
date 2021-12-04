class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        self.alkuarvo = self.sovellus.tulos
        return self.sovellus.plus(self.io())
    
    def kumoa(self):
        return self.sovellus.aseta_arvo(self.alkuarvo)


class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        self.alkuarvo = self.sovellus.tulos
        return self.sovellus.miinus(self.io())
    
    def kumoa(self):
        return self.sovellus.aseta_arvo(self.alkuarvo)


class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.alkuarvo = self.sovellus.tulos
        return self.sovellus.nollaa()
