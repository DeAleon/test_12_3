import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.user_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.user_2 = runner_and_tournament.Runner('Андрей', 9)
        self.user_3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        turn = runner_and_tournament.Tournament(90, self.user_1, self.user_3)
        results = turn.start()
        self.assertTrue(results[max(results.keys())] == "Ник")
        self.all_results[1] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        turn = runner_and_tournament.Tournament(90, self.user_2, self.user_3)
        results = turn.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        turn = runner_and_tournament.Tournament(90, self.user_1, self.user_2, self.user_3)
        results = turn.start()
        self.assertTrue(results[max(results.keys())] == "Ник")
        self.all_results[3] = results

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(v)