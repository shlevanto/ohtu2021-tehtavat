class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        self.alkuarvo = self.sovellus.tulos
        print(self.alkuarvo)
        return self.sovellus.plus(self.io())
    
    def kumoa(self):
        return self.alkuarvo

class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.miinus(self.io())

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, syote):
        pass
    def suorita(self, sovellus, syote):
        return sovellus.nollaa(syote)