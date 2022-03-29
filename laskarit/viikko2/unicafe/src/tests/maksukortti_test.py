import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_maksukortin_arvo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(140)
        self.assertEqual(str(self.maksukortti), "saldo: 11.4")
    
    def test_onnistunut_rahan_ottaminen_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_epaonnistunut_rahan_ottaminen_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)
    
    def test_raha_vahenee_otettaessa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_raha_ei_vahene_jos_yritetaan_vahentaa_liikaa(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")