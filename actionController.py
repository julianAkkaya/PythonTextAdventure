import actions
from help import help

def controller(actionInput, player, welt):
    if actionInput == "north":
        nextPlaceId = player.currentPlace.north[1]
        actions.go(nextPlaceId, player, welt)
    elif actionInput == "east":
        nextPlaceId = player.currentPlace.east[1]
        actions.go(nextPlaceId, player, welt)
    elif actionInput == "south":
        nextPlaceId = player.currentPlace.south[1]
        actions.go(nextPlaceId, player, welt)
    elif actionInput == "west":
        nextPlaceId = player.currentPlace.west[1]
        actions.go(nextPlaceId, player, welt)
    elif actionInput == "help":
        help()
    else:
        print "Ich befuerchte das geht nicht?!"