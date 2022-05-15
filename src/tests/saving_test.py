import unittest
from score_saving import ScoreSaving,dirname
import os

class TestSaving(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(dirname, "assets", "score.txt"), "w",
                      encoding="utf-8") as file:
                file.write("")

    def test_reading_empty_returns_zero(self):
        self.assertEqual(ScoreSaving().read_score(),0)

    def test_saving_new_score_changes_score(self):
        ScoreSaving().save_score(100)
        self.assertEqual(ScoreSaving().read_score(),100)
    
    def test_saving_lower_score_doesnt_save(self):
        ScoreSaving().save_score(100)
        ScoreSaving().save_score(50)
        self.assertEqual(ScoreSaving().read_score(),100)
        with open(os.path.join(dirname, "assets", "score.txt"), "w",
                      encoding="utf-8") as file:
                file.write("")
