from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        self.tavaroiden_maara = 0
        self.arvo = 0
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroiden_maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.arvo
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self.tavaroiden_maara += 1
        self.arvo += lisattava.hinta()
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
               return
        return

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
