#Задача "Проверка на выносливость"
import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        object_1 = runner.Runner('Vanya')
        for i in range(1, 11):
            object_1.walk()
        self.assertEqual(object_1.distance, 50)
    def test_run(self):
        object_2 = runner.Runner('Varya')
        for i in range(1, 11):
            object_2.run()
        self.assertEqual(object_2.distance, 100)
    def test_challenge(self):
        object_3 = runner.Runner('Zero')
        object_4 = runner.Runner('Null')
        for i in range(1, 11):
            object_3.run()
            object_4.walk()
        self.assertNotEqual(object_3.distance, object_4.distance)

