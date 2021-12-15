from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSFactory:
    
    @staticmethod
    def pelaa_kaksi_pelaajaa():
        kaksinpeli = KPSPelaajaVsPelaaja()
        return kaksinpeli

    @staticmethod
    def pelaa_tekoaly():
        tekoalypeli = KPSTekoaly()
        return tekoalypeli
    
    @staticmethod
    def pelaa_parempi_tekoaly():
        parempi_tekoalypeli = KPSParempiTekoaly()
        return parempi_tekoalypeli