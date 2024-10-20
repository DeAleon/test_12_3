import runner
import unittest


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tw = runner.Runner('Test1')
        for walk in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tr = runner.Runner('Test2')
        for run in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tw = runner.Runner('Test1')
        tr = runner.Runner('Test2')
        for walk in range(10):
            tw.walk()
        for run in range(10):
            tr.run()
        self.assertNotEqual(tw.distance, tr.distance)


if __name__ == '__main__':
    unittest.main()
