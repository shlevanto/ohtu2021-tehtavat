

class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self, arvo):
        return self.sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self, arvo):
        return self.sovellus.miinus(arvo)

class Nollaus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self, arvo):
        return self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, syote):
        pass
    def suorita(self, sovellus, syote):
        return sovellus.nollaa(syote)