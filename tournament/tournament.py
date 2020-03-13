def tally(rows):
    results = [row.split(';') for row in rows]
    teams = {}
    for result in results:
        if result[0] not in teams:
            teams[result[0]] = Team(result[0])
        if result[1] not in teams:
            teams[result[1]] = Team(result[1])
        if result[2] == 'win':
            teams[result[0]].setResult(1)
            teams[result[1]].setResult(-1)
        elif result[2] == 'loss':
            teams[result[0]].setResult(-1)
            teams[result[1]].setResult(1)
        else:
            teams[result[0]].setResult(0)
            teams[result[1]].setResult(0)
    table = ['Team                           | MP |  W |  D |  L |  P']
    for team in teams:
        teams[team].calcPoints()
    teams = sorted([teams[team] for team in teams], reverse=True)
    for team in teams:
        print(team.display())
    return table + [team.display() for team in teams]


class Team(object):
    def __init__(self, name):
        self.name = name
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def __gt__(self, other):
        if self.points > other.points:
            return True
        elif self.points < other.points:
            return False
        else:
            if self.name > other.name:
                return False
            else:
                return True

    def display(self):
        line = '{}|  {} |  {} |  {} |  {} |  {}'
        return line.format(self.name.ljust(31), self.matches, self.wins,
                           self.draws, self. losses, self.points)

    def setResult(self, result):
        self.matches += 1
        if result == 1:
            self.wins += 1
        elif result == -1:
            self.losses += 1
        else:
            self.draws += 1

    def calcPoints(self):
        self.points = self.wins * 3 + self.draws