import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(maito.hinta(), self.kori.hinta())

    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_arvo_on_tuotteiden_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tavaran_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tavaran_lisaamisen_jalkeen_korin_arvo_on_sama_kuin_kahden_tavaran(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tavaran_lisaamisen_jalkeen_ostoksia_on_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tavaran_lisaamisen_jalkeen_ostoksella_on_sama_nimi_ja_lukumaara_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "Maito")
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)

    def test_kaksi_samaa_tuotetta_toinen_poistetaan_jaa_yksi_ostos_jossa_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    def test_lisaa_yksi_tuote_ja_poista_se_ostoskori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_clear_tyhjentaa_ostoskorin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(juusto)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)



    