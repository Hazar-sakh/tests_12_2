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
                if self.full_distance >= 7 and participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                # ДОПОЛНИТЕЛЬНО
                elif self.full_distance < 7:
                    spd = []
                    for i in self.participants:
                        spd.append([i.speed, i.name])
                    spd.sort(reverse=True)
                    pl = 1
                    for i in spd:
                        i[0] = pl
                        pl += 1
                    finishers.update(spd)
                    self.participants.clear()

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.U = Runner('Усейн', 10)
        self.A = Runner('Андрей', 9)
        self.N = Runner('Ник', 3)

    def resulter(self, args):
        res = []
        for key, value in args.items():
            res.append((key, str(value)))
        all_results.update(res)
        print(self.tearDownClass())

    def test_1(self):
        d1 = Tournament(90, self.U, self.N)
        r1 = d1.start()
        self.resulter(r1)
        self.assertTrue(r1[2] == 'Ник', f'Ошибка: {r1[1]} не может быть последним!')

    def test_2(self):
        d2 = Tournament(90, self.A, self.N)
        r2 = d2.start()
        self.resulter(r2)
        self.assertTrue(r2[2] == 'Ник', f'Ошибка: {r2[1]} не может быть последним!')

    def test_3(self):
        d3 = Tournament(90, self.U, self.A, self.N)
        r3 = d3.start()
        self.resulter(r3)
        self.assertTrue(r3[3] == 'Ник', f'Ошибка: {r3[3]} не может быть последним!')

    #ДОПОЛНИТЕЛЬНО
    def test_4(self):
        d4 = Tournament(6, self.U, self.A, self.N)
        r4 = d4.start()
        self.resulter(r4)
        self.assertTrue(r4[3] == 'Ник', f'Ошибка: {r4[3]} не может быть последним!')

    @classmethod
    def tearDownClass(cls):
        return all_results


if __name__ == '__main__':
    unittest.main
