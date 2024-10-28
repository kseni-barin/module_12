# tests_12_1:

import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        object_1 = runner.Runner('Vanya')
        for i in range(1, 11):
            object_1.walk()
        self.assertEqual(object_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        object_2 = runner.Runner('Varya')
        for i in range(1, 11):
            object_2.run()
        self.assertEqual(object_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        object_3 = runner.Runner('Zero')
        object_4 = runner.Runner('Null')
        for i in range(1, 11):
            object_3.run()
            object_4.walk()
        self.assertNotEqual(object_3.distance, object_4.distance)


# tests_12_2:
import test as rt
import unittest

class TournamentTest(unittest.TestCase):

    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_1_start(self):
        tournament_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update(tournament_1.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_2_start(self):
        tournament_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update(tournament_2.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_3_start(self):
        tournament_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update(tournament_3.start())
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)


