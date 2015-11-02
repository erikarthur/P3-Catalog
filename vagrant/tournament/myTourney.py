__author__ = 'erik'

from tournament import Tournament
import math
import random

t = Tournament()
db = t.connect()
t.deletePlayers(db)
t.deleteMatches(db)

t.registerPlayer("Ace", db)
t.registerPlayer("Jimmy", db)
t.registerPlayer("Phil", db)
t.registerPlayer("Sport", db)
t.registerPlayer("Ed", db)
t.registerPlayer("Lucy", db)
t.registerPlayer("Jake", db)
t.registerPlayer("Adam", db)

count = t.countPlayers(db)
rounds = int(math.log(count, 2))
currentRound = 0
# if int(math.log(count,2)) == round(math.log(count,2)):
#     print "int"

for x in range(0, rounds):

    print 'Round {0} Matches\n'.format(x+1)

    playerPairings = t.swissPairings(db)

    for playerPair in playerPairings:

        if random.random() < .5:
            # first player won
            t.reportMatch(db, playerPair[0], playerPair[2])
            print 'Winner: {0}\tLoser: {1}'.format(playerPair[1], playerPair[3])

        else:
            # second player won
            t.reportMatch(db, playerPair[2], playerPair[0])
            print 'Winner: {0}\tLoser: {1}'.format(playerPair[3], playerPair[1])

    standings = t.playerStandings(db)


