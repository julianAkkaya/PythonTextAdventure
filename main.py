from player import Player
import places
import actionController

victory = False

welt = places.Welt()

you = Player()
you.currentPlace = welt.dorfplatz


while victory == False and you.alive == True:
    print "\n"
    actionInput = raw_input("Dein Input:")
    actionController.controller(actionInput, you, welt)