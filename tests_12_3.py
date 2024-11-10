import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
             return method(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @skip_if_frozen
    def test_sprint1(self):
        sprint_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results[1] = sprint_1.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[1][2], 'Ник')

    @skip_if_frozen
    def test_sprint2(self):
        sprint_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results[2] = sprint_2.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[2][2], 'Ник')

    @skip_if_frozen
    def test_sprint3(self):
        sprint_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results[3] = sprint_3.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[3][3], 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Test Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()  # 10 * 10 = 100
            runner2.walk()  # 10 * 5 = 50

        self.assertNotEqual(runner1.distance, runner2.distance)

    if __name__ == "__main__":
        unittest.main()