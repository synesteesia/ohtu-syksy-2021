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
		self.statistics = Statistics(
			PlayerReaderStub()
		)

	def test_search_toimii(self):
		self.assertEqual(self.statistics.search("Gretzky").__str__(), "Gretzky EDM 35 + 89 = 124")

	def test_search_toimii_kun_ei_loydy(self):
		self.assertEqual(self.statistics.search("Pekka").__str__(), "None")

	def test_team_toimii(self):
		self.assertEqual(self.statistics.team("EDM")[2].__str__(), "Gretzky EDM 35 + 89 = 124")

	def test_team_toimii_kun_ei_loydy(self):
		self.assertEqual(self.statistics.team("KEK"), [])

	def test_top_toimii(self):
		self.assertEqual(self.statistics.top_scorers(4)[0].__str__(), "Gretzky EDM 35 + 89 = 124")
		self.assertEqual(self.statistics.top_scorers(4)[3].__str__(), "Kurri EDM 37 + 53 = 90")
		self.assertEqual(self.statistics.top_scorers(4)[4].__str__(), "Semenko EDM 4 + 12 = 16")



