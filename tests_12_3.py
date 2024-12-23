import unittest
from HumanMoveTest import runner
import rr
import Runner
import runner_and_tournament as rt

# объявление функции декоратора frozen для проверки атрибута is_frozen
def frozen(func):
    def wrapper(atr):
        # проверка атрибута is_frozen на True или False
        if atr.is_frozen == True:
            # если True - пропуск методов декорирования
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            # если False - выполнение методов декорирования
            return func

    # возврат выполнения wrapper
    return wrapper


class TournamentTest(unittest.TestCase):
        is_frozen = True
        all_results = None

        # setUpClass - метод, где создаётся атрибут класса all_results.
        @classmethod
        def setUpClass(cls):
                # словарь в который будут сохраняться результаты всех тестов.
                cls.all_results = {}

        @frozen
        def setUp(self):
                self.run1 = rt.Runner('Усэйн', 10)
                self.run2 = rt.Runner('Андрей', 9)
                self.run3 = rt.Runner('Ник', 3)
                self.run4 = rt.Runner('Алекс', 5)

        @classmethod
        def tearDownClass(cls):
                result = {}
                for testkey, testval in cls.all_results.items():
                        print(f'TEST: {testkey}')
                        for key, val in testval.items():
                                result[key] = str(val.name)
                        print(result)

        @frozen
        def test_first_tournament(self):
                run_1 = rt.Tournament(90, self.run1, self.run3)
                finish = run_1.start()
                self.assertTrue(list(finish.values())[-1].name == str(self.run3))
                self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

        @frozen
        def test_second_tournament(self):
                run_1 = rt.Tournament(90, self.run2, self.run3)
                finish = run_1.start()
                self.assertTrue(list(finish.values())[-1].name == str(self.run3))
                self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

        @frozen
        def test_third_tournament(self):
                run_1 = rt.Tournament(90, self.run1, self.run2, self.run3)
                finish = run_1.start()
                self.assertTrue(list(finish.values())[-1].name == str(self.run3))
                self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen
    def test_walk(self):
        walk_ = rr.Runner('man')
        for _ in range(10):
            walk_.walk()
        self.assertEqual(walk_.distance, 50)
        print('Test "walk" OK')

    @frozen
    def test_run(self):
        run_ = rr.Runner('man')
        for _ in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)
        print('Test "run" OK')

    @frozen
    def test_challenge(self):
        challenge1 = rr.Runner('man_R')
        challenge2 = rr.Runner('man_W')
        for _ in range(10):
            challenge1.run()
            challenge2.walk()
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        print('Test "challenge" OK')


if __name__ == "__main__":
        unittest.main()



