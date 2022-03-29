import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.paate, None)
    
    def test_uuden_paatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_uuden_paatteen_myydyt_edulliset_on_oikea(self):
        self.assertEqual(self.paate.edulliset, 0)
    
    def test_uuden_paatteen_myydyt_maukkaat_on_oikea(self):
        self.assertEqual(self.paate.maukkaat, 0)
    
    #käteinen, edulliset
    
    def test_kateisella_edullisesti_vaihtoraha(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(250), 10)
    
    def test_kateisella_edullisesti_kassan_raha_kasvaa(self):
        self.paate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
    
    def test_kateisella_edullisesti_lounaat_kasvaa(self):
        self.paate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.paate.edulliset, 1)
    
    def test_kateisella_edullisesti_palautus_kun_ei_tarpeeksi(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(220), 220)

    def test_kateisella_edullisesti_kassa_ei_kasva_kun_ei_tarpeeksi(self):
        self.paate.syo_edullisesti_kateisella(220)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateisella_edullisesti_lounaat_ei_kasva_kun_ei_tarpeeksi(self):
        self.paate.syo_edullisesti_kateisella(220)
        self.assertEqual(self.paate.edulliset, 0)

    #maukkaat


    
    def test_kateisella_maukkaasti_vaihtoraha(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(440), 40)
    
    def test_kateisella_maukkaasti_kassan_raha_kasvaa(self):
        self.paate.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
    
    def test_kateisella_maukkaasti_lounaat_kasvaa(self):
        self.paate.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.paate.maukkaat, 1)
    
    def test_kateisella_maukkaasti_palautus_kun_ei_tarpeeksi(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(220), 220)

    def test_kateisella_maukkaasti_kassa_ei_kasva_kun_ei_tarpeeksi(self):
        self.paate.syo_maukkaasti_kateisella(220)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateisella_maukkaasti_lounaat_ei_kasva_kun_ei_tarpeeksi(self):
        self.paate.syo_maukkaasti_kateisella(220)
        self.assertEqual(self.paate.maukkaat, 0)
    
    #kortti, edullinen

    def test_onnistunut_edullinen_kortti_palauttaa_true(self):
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti),True)
    
    def test_onnistunut_edullinen_kortti_veloittaa_kortilta(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 7.6")
    
    def test_onnistunut_edullinen_kortti_nostaa_myytyja(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 1)

    def test_epaonnistunut_edullinen_kortti_palauttaa_false(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti),False)

    def test_epaonnistunut_edullinen_kortti_ei_veloita_kortilta(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.4")
    
    def test_epaonnistunut_edullinen_kortti_ei_nosta_myytyja(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 0)
    
    #kortti, maukas

    def test_onnistunut_maukas_kortti_palauttaa_true(self):
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti),True)
    
    def test_onnistunut_maukas_kortti_veloittaa_kortilta(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 6.0")
    
    def test_onnistunut_maukas_kortti_nostaa_myytyja(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_epaonnistunut_maukas_kortti_palauttaa_false(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti),False)

    def test_epaonnistunut_maukas_kortti_ei_veloita_kortilta(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
    
    def test_epaonnistunut_maukas_kortti_ei_nosta_myytyja(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 2)

    #kortti, yleinen tilanne + lataus

    def test_kortti_ei_nosta_kateista(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_rahan_lataus_muuttaa_kortin_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,500)
        self.assertEqual(str(self.kortti), "saldo: 15.0")
    
    def test_rahan_lataus_muuttaa_kassan_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,500)
        self.assertEqual(self.paate.kassassa_rahaa, 100500)
    
    def test_negatiivinen_rahan_lataus_ei_muuta_kortin_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,-500)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
    
    def test_negatiivinen_rahan_lataus_ei_muuta_kassan_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,-500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        



