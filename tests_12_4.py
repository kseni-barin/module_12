#Задача "Логирование бегунов"
import rt_with_exceptions as runner
import unittest
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            object_1 = runner.Runner('Vanya', -10)
            for i in range(1, 11):
                object_1.walk()
            self.assertEqual(object_1.distance, 100)
            logging.info(f'test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            object_2 = runner.Runner(67, 5)
            for i in range(1, 11):
                object_2.run()
            self.assertEqual(object_2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')


