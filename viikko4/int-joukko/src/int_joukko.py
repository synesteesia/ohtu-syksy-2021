KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla nollaa suuremi kokonaisluku")  
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla nollaa suuremi kokonaisluku") 
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0


    def kuuluuko_joukkoon(self, alkio):
        for i in range(self.alkioiden_lkm):
            if alkio == self.joukko[i]:
                return True
        return False


    def kasvata_kapasiteettia(self):
        self.kasvatuskoko *= 2
        uusi_joukko = [0] * (self.kasvatuskoko)
        for i in range(len(self.joukko)):
            uusi_joukko[i] = self.joukko[i]
        self.joukko = uusi_joukko


    def lisaa_alkio(self, alkio):
        if not self.kuuluuko_joukkoon(alkio):
            self.joukko[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.joukko):
                self.kasvata_kapasiteettia()
            return True
        return False

    def poista_alkio(self, alkio):
        for i in range(self.alkioiden_lkm):
            if alkio == self.joukko[i]:
                for j in range(i, self.alkioiden_lkm - 1):
                   apu = self.joukko[j]
                   self.joukko[j] = self.joukko[j + 1]
                   self.joukko[j + 1] = apu
                self.alkioiden_lkm -= 1
                return True
        return False

    def alkioiden_maara(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(len(taulu)):
            taulu[i] = self.joukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            yhdiste.lisaa_alkio(a_joukko[i])

        for i in range(len(b_joukko)):
            yhdiste.lisaa_alkio(b_joukko[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            for j in range(0, len(b_joukko)):
                if a_joukko[i] == b_joukko[j]:
                    leikkaus.lisaa_alkio(b_joukko[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            erotus.lisaa_alkio(a_joukko[i])

        for i in range(len(b_joukko)):
            erotus.poista_alkio(b_joukko[i])

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.joukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
