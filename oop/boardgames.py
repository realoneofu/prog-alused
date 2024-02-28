"""Board games."""


class Player:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.played = {}
        self.favourite = ""
        self.won = 0
        self.lost = 0

    def win(self):
        self.won += 1

    def lose(self):
        self.lost += 1

    def play(self, game):
        self.amount += 1
        if game not in self.played:
            self.played[game] = 0
        self.played[game] += 1


class Game:
    def __init__(self, game, result):
        self.game = game
        self.players = []
        self.winners = []
        self.losers = []
        self.result = result
        self.played = 0
        self.most = 0
        self.record = 0
        self.recordholder = ""

    def play(self, players):
        self.played += 1
        if len(players) > self.most:
            self.most = len(players)

    def win(self, player):
        self.winners.append(player)

    def lose(self, player):
        self.losers.append(player)

    def recordd(self, player, points):
        if points > self.record:
            self.record = points
            self.recordholder = player


class Statistics:
    def __init__(self, filename):
        self.players = {}
        self.games = {}
        self.total = 0
        self.data = open(filename, "r").readlines()
        for i in self.data:
            v = i.strip().split(";")
            if v[0] not in self.games:
                self.games[v[0]] = Game(v[0], v[2])
            self.games[v[0]].play(v[1].split(","))
            for plr in v[1].split(","):
                if plr not in self.players:
                    self.players[plr] = Player(plr)
                self.players[plr].play(v[0])
            if v[2] == "winner":
                winner = v[3]
                self.players[winner].win()
                self.games[v[0]].win(winner)
            elif v[2] == "points":
                results = {}
                points = v[3].split(",")
                winner = None
                loser = None
                for plr in v[1].split(","):
                    results[points[v[1].split(",").index(plr)]] = plr
                lb = 0
                for plr in results.keys():
                    if int(plr) > lb:
                        lb = int(plr)
                        winner = results[plr]
                ls = 4294967296
                for plr in results.keys():
                    if int(plr) < ls:
                        ls = int(plr)
                        loser = results[plr]
                self.players[winner].win()
                self.games[v[0]].win(winner)
                self.games[v[0]].recordd(winner, lb)
                self.players[loser].lose()
                self.games[v[0]].lose(loser)
            elif v[2] == "places":
                winner = v[3].split(",")[0]
                self.players[winner].win()
                self.games[v[0]].win(winner)
                loser = v[3].split(",")[-1]
                self.players[winner].lose()
                self.games[v[0]].lose(loser)

    def get(self, path: str):
        pth = path.split("/")
        pth.pop(0)
        if pth[0] == "players":
            return list(self.players.keys())
        elif pth[0] == "games":
            return list(self.games.keys())
        elif pth[0] == "total":
            if len(pth) > 1:
                arg2 = pth[1]
                ttl = 0
                for game in self.data:
                    rvar = game.split(";")
                    if rvar[2] == arg2:
                        ttl += 1
                return ttl
            else:
                return len(self.data)
        elif pth[0] == "player":
            plr = self.players[pth[1]]
            arg2 = pth[2]
            if arg2 == "amount":
                return plr.amount
            elif arg2 == "favourite":
                lb = 0
                mplayed = None
                for game in plr.played:
                    if int(plr.played[game]) > lb:
                        lb = int(plr.played[game])
                        mplayed = game
                return mplayed
            elif arg2 == "won":
                return plr.won
        elif pth[0] == "game":
            game = self.games[pth[1]]
            arg2 = pth[2]
            if arg2 == "amount":
                return game.played
            elif arg2 == "player-amount":
                return game.most
            elif arg2 == "most-wins":
                most = 0
                mostw = None
                for plr in sorted(game.winners):
                    if game.winners.count(plr) > most:
                        most = game.winners.count(plr)
                        mostw = plr
                return mostw
            elif arg2 == "most-frequent-winner":
                most = 0
                mostw = None
                for plr in sorted(game.winners):
                    if (game.winners.count(plr) / self.players[plr].amount) > most:
                        most = game.winners.count(plr) / self.players[plr].amount
                        mostw = plr
                return mostw
            elif arg2 == "most-losses":
                most = 0
                mostw = None
                for plr in sorted(game.losers):
                    if game.losers.count(plr) > most:
                        most = game.losers.count(plr)
                        mostw = plr
                return mostw
            elif arg2 == "most-frequent-loser":
                most = 0
                mostw = None
                for plr in sorted(game.losers):
                    if (game.losers.count(plr) / self.players[plr].amount) > most:
                        most = game.losers.count(plr) / self.players[plr].amount
                        mostw = plr
                return mostw
            elif arg2 == "record-holder":
                return game.recordholder

xd = Statistics("bgdata.txt")
print(xd.get("/total/points"))