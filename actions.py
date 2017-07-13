def go (nextPlaceId, player, welt):
    safeCurrentPlace(player, welt)
    changePlace(nextPlaceId, player, welt)
    printNewLocation(player)

def safeCurrentPlace(player, welt):
    if player.currentPlace.currentId == 1:
        welt.dorfplatz = player.currentPlace
    if player.currentPlace.currentId == 2:
        welt.baeker = player.currentPlace

def printNewLocation(player):
    print player.currentPlace.description
    print "\n"
    print "north: " + player.currentPlace.north[0]
    print "east: " + player.currentPlace.east[0]
    print "south: " + player.currentPlace.south[0]
    print "west: " + player.currentPlace.west[0]
    print "\n"

def changePlace(nextPlaceId, player, welt):
    if nextPlaceId == 0:
        print "Das ist nicht moeglich."
    elif nextPlaceId == 1:
        player.currentPlace = welt.dorfplatz
    elif nextPlaceId == 2:
        player.currentPlace = welt.baeker
