import random
class Gold ():
    def __init__(self, worth):
        self.worth = worth
        self.description = "kleine goldklumpen im wert von " + str(self.worth)

    def add(self, value):
        self.worth += value
        if self.worth <= 0:
            self.worth = 0
            print "Du hast dein Gold nochmal genauer untersucht und du bist pleite."
        else:
            print("Das Gold scheint doch mehr wert zu sein als du anfangs dachtest, " + str(self.worth))


    def sub(self, value):
        self.worth -= value
        if self.worth <= 0:
            self.worth = 0
            print "Du hast dein Gold nochmal genauer untersucht und du bist pleite."
        else:
            print("Das Gold scheint doch weniger wert zu sein als du anfangs dachtest, " + str(self.worth))

    def study(self):
        value = round(random.random() * 4 + 1, 2)
        if random.choice([0, 1]):
            self.add(value)
        else:
            self.sub(value)