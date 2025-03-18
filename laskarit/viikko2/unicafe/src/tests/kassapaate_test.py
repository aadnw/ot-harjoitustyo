import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_rahamaara_on_luodessa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara_on_luodessa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_on_luodessa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahat_riittavat_edulliseen_kateisella_ja_vaihtoraha_on_oikein(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(vastaus, 260)

    def test_kassan_rahamaara_kasvaa_edullisesta_lounaasta(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_myytyjen_edullisten_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_rahat_eivat_riita_edulliseen_kateisella_ja_rahat_palautetaan(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(vastaus, 100)

    def test_kassan_rahamaara_ei_muutu_jos_rahat_eivat_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_maara_ei_muutu_jos_rahat_eivat_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_rahat_riittavat_maukkaaseen_kateisella_ja_vaihtoraha_on_oikein(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vastaus, 100)

    def test_kassan_rahamaara_kasvaa_maukkaasta_lounaasta(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_myytyjen_maukkaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahat_eivat_riita_maukkaaseen_kateisella_ja_rahat_palautetaan(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(vastaus, 100)

    def test_kassan_rahamaara_ei_muutu_jos_rahat_eivat_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_maukkaiden_maara_ei_muutu_jos_rahat_eivat_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahat_riittävät_edulliseen_kortilla(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(vastaus, True)

    def test_rahat_riittavat_edulliseen_kortilla_ja_kortilta_veloitetaan_oikea_summa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

    def test_myytyjen_edullisten_maara_kasvaa_kortilla_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_rahat_eivät_riitä_edulliseen_kortilla(self):
        kortti = Maksukortti(0)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(vastaus, False)

    def test_kortin_rahamaara_ei_muutu_jos_rahat_eivat_riita_edulliseen(self):
        kortti = Maksukortti(0)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_myytyjen_edullisten_maara_ei_muutu_jos_rahat_kortilla_eivat_riita(self):
        kortti = Maksukortti(0)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_rahamaara_ei_muutu_kun_ostetaan_edullinen_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahat_riittävät_maukkaaseen_kortilla(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(vastaus, True)

    def test_rahat_riittavat_maukkaaseen_kortilla_ja_kortilta_veloitetaan_oikea_summa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_myytyjen_maukkaiden_maara_kasvaa_kortilla_ostettaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahat_eivät_riitä_maukkaaseen_kortilla(self):
        kortti = Maksukortti(0)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(vastaus, False)

    def test_kortin_rahamaara_ei_muutu_jos_rahat_eivat_riita_maukkaaseen(self):
        kortti = Maksukortti(0)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_myytyjen_maukkaiden_maara_ei_muutu_jos_rahat_kortilla_eivat_riita(self):
        kortti = Maksukortti(0)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_kun_ostetaan_maukas_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahaa_ladattaessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_rahaa_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassan_saldo_euroina_on_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)