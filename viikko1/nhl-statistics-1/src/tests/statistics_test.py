import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        present = self.statistics.search("Semenko").name
        absent = self.statistics.search("Virtanen")

        self.assertEqual(present, "Semenko")
        self.assertEqual(absent, None)

    def test_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_top_scorers(self):
        top_three = self.statistics.top_scorers(2)
        best_player = top_three[0]

        self.assertEqual(len(top_three), 3)
        self.assertEqual(best_player.name, "Gretzky")