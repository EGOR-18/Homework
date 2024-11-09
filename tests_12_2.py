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


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_sprint1(self):
        sprint_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results[1] = sprint_1.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[1][2], 'Ник')

    def test_sprint2(self):
        sprint_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results[2] = sprint_2.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[2][2], 'Ник')

    def test_sprint3(self):
        sprint_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results[3] = sprint_3.start()
        unittest.TestCase.assertEqual(self, TournamentTest.all_results[3][3], 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    if __name__ == "__main__":
        unittest.main()