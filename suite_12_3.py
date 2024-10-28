import unittest
import tests_12_1
import tests_12_2

tests_TS = unittest.TestSuite()

tests_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tests_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests_TS)

