
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Virheellinen kapasiteetti.") 
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Virheellinen kasvatuskoko.")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        # helpoin
        # return n in self.ljono[0:self.alkioiden_lkm]

        # alkuperäisen hengen mukainen
        for i in range(0, self.alkioiden_lkm + 1):
            if self.ljono[i] == n:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        if len(self.ljono) % self.alkioiden_lkm == 0:
            # helppo
            # self.ljono += [0] * self.kapasiteetti

            # alkuperäisen hengen mukainen, luo uuden taulukon
            uusi = [0] * (len(self.ljono) + self.kasvatuskoko)
            for i in range(0, self.alkioiden_lkm):
                uusi[i] = self.ljono[i]
            self.ljono = uusi

        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        # helppo
        # self.ljono.remove(n)
        # self.alkioiden_lkm -= 1

        # alkuperäisen hengen mukainen
        kohta = 0

        for i in self.ljono:
            if i == n:
                print(kohta)
                break
            kohta += 1

        self.ljono = self.ljono[:kohta] + self.ljono[kohta+1:]
        self.alkioiden_lkm -= 1

        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        for i in a.to_int_list():
            b.lisaa(i)
        return b

    @staticmethod
    def leikkaus(a, b):
        for i in a.to_int_list():
            if not b.kuuluu(i):
                a.poista(i)
        return a

    @staticmethod
    def erotus(a, b):
        for i in b.to_int_list():
            a.poista(i)
        return a

    def __str__(self):
        return '{' + str(self.to_int_list())[1:-1] + '}'
