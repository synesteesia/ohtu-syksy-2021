from enum import Enum
from tkinter import ttk, constants, StringVar

from sovelluslogiikka import Sovelluslogiikka


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovellus = sovelluslogiikka
        self._root = root

        self._kommenot = {
        Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
        Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
        Komento.NOLLAUS: Nollaus(sovelluslogiikka),
        Komento.KUMOA: Kumoa(sovelluslogiikka)
        }    

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA),
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)



    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._kommenot[komento]
        komento_olio.suorita()
        if type(komento_olio).__name__ != 'Kumoa':
            self._kommenot[Komento.KUMOA].paivita(komento_olio)

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)


class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.arvot = []

    def suorita(self):
        self.arvot.append(int(self.syote()))
        self.sovellus.plus(self.arvot[-1])

    def kumoa(self):
        if len(self.arvot) > 0:
            self.sovellus.miinus(self.arvot.pop())



class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.arvot = []

    def suorita(self):
        self.arvot.append(int(self.syote()))
        self.sovellus.miinus(self.arvot[-1])

    def kumoa(self):
        if len(self.arvot) > 0:
            self.sovellus.plus(self.arvot.pop())



class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka
        self.arvot = []


    def suorita(self):
        self.arvot.append(self.sovellus.tulos)
        self.sovellus.nollaa()

    def kumoa(self):
        if len(self.arvot) > 0:
            self.sovellus.plus(self.arvot.pop())


class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka
        self.komennot = []

    def suorita(self):
        if len(self.komennot) > 0:
            self.komennot.pop().kumoa()

    def paivita(self, komento):
        self.komennot.append(komento)
