import unittest
import tests_12_3


suite = unittest.TestSuite()
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
