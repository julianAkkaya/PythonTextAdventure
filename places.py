class Welt():
    def __init__(self):
        self.dorfplatz = Dorfplatz()
        self.baeker = Baeker()


class Dorfplatz():
    def __init__(self):
        self.currentId = 1
        self.west = ["Zum Baecker", 2]
        self.east = ["Hier geht es nicht lang", 0]
        self.south = ["Hier geht es nicht lang", 0]
        self.north = ["Hier geht es nicht lang", 0]
        self.description = "Du Steht auf dem Dorfplatz, die Sonne Scheint."


class Baeker():
    def __init__(self):
        self.currentId = 2
        self.east = ["Zum Dorfplatz", 1]
        self.west = ["Hier geht es nicht lang", 0]
        self.south = ["Hier geht es nicht lang", 0]
        self.north = ["Hier geht es nicht lang", 0]
        self.description = "Du stehst in der Baeckerei, es riecht hier wunderbar nach Brot."