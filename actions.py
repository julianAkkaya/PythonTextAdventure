def go (nextPlaceId, player, welt):
    safeCurrentPlace(player, welt)
    changePlace(nextPlaceId, player, welt)

def safeCurrentPlace(player, welt):
    currentPlace = player.currentPlace.currentId
    if currentPlace == 1:
        welt.baeker = player.currentPlace
    if currentPlace == 2:
        welt.dorfplatz = player.currentPlace

def changePlace(nextPlaceId, player, welt):
    if nextPlaceId == 0:
        print "Das ist nicht moeglich."
    elif nextPlaceId == 1:
        player.currentPlace = welt.dorfplatz
        print player.currentPlace.description
    elif nextPlaceId == 2:
        player.currentPlace = welt.baeker
        print player.currentPlace.description