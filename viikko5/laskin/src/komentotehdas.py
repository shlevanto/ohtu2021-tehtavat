

class Summa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote
        
    def suorita(self):
        print(self.syote)
        #return self.sovellus.plus(self.syote)

class Erotus:
    def __init__(self, sovellus, syote):
        pass
    def suorita(self, sovellus, syote):
        return sovellus.miinus(syote)

class Nollaus:
    def __init__(self, sovellus, syote):
        pass
    def suorita(self, sovellus, syote):
        return sovellus.nollaa(syote)

class Kumoa:
    def __init__(self, sovellus, syote):
        pass
    def suorita(self, sovellus, syote):
        return sovellus.nollaa(syote)