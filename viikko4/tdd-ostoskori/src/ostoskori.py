from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for i in range(len(self.ostokset())):
            maara += self._ostokset[i].lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        arvo = 0
        for i in range(len(self.ostokset())):
            arvo += self._ostokset[i].hinta()
        return arvo
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if self.tuote_loytyy(lisattava):
           return
        else:
           self._ostokset.append(Ostos(lisattava))
           # lisää tuotteen

    def tuote_loytyy(self, lisattava: Tuote):
        for i in range(len(self.ostokset())):
            if lisattava.nimi() == self._ostokset[i].tuotteen_nimi():
               self._ostokset[i].muuta_lukumaaraa(1)
               return True
        return False

    def poista_tuote(self, poistettava: Tuote):
        for i in range(len(self.ostokset())):
            if poistettava.nimi() == self._ostokset[i].tuotteen_nimi():
               self._ostokset[i].muuta_lukumaaraa(-1)
               if self._ostokset[i].lukumaara() == 0:
                  del self._ostokset[i]
        return

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
