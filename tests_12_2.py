import test as rt
import unittest

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @classmethod
    def tearDownClass(self):
        for result, value in self.all_results.items():
            print(f"{result} : {value}")

    def test_1_start(self):
        tournament_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update(tournament_1.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)

    def test_2_start(self):
        tournament_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update(tournament_2.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)

    def test_3_start(self):
        tournament_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update(tournament_3.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)

    def test_sort_speed(self):
        tournament_5 = rt.Tournament(9,  self.runner_2, self.runner_1, self.runner_3)
        list_part_speed = tournament_5.sort_part()
        self.assertGreaterEqual(list_part_speed[0].speed, list_part_speed[1].speed)
        self.assertGreaterEqual(list_part_speed[1].speed, list_part_speed[2].speed)

    def test_start_participants(self):
        tournament_4 = rt.Tournament(9,  self.runner_2, self.runner_1, self.runner_3)
        result = tournament_4.start()
        self.assertEqual(result[1], self.runner_1)

