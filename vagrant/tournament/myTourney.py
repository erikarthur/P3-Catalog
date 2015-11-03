__author__ = 'erik'

from tournament import *
import math
import random
import decimal


db = connect()
deletePlayers()
deleteMatches()

registerPlayer("Ace")
registerPlayer("Jimmy")
registerPlayer("Phil")
registerPlayer("Sport")
registerPlayer("Ed")
registerPlayer("Lucy")
registerPlayer("Jake")
registerPlayer("Adam")
registerPlayer("Ace2")
registerPlayer("Jimmy2")
registerPlayer("Phil2")
registerPlayer("Sport2")
registerPlayer("Ed2")
registerPlayer("Lucy2")
registerPlayer("Jake2")
registerPlayer("Adam2")
# t.registerPlayer("Jake3", db)
# t.registerPlayer("Adam3", db)

count = countPlayers()
rounds = int(math.ceil(math.log(count,2)))

currentRound = 0

for x in range(0, rounds):

    print 'Round {0} Matches\n'.format(x+1)

    playerPairings = swissPairings()

    for playerPair in playerPairings:

        if random.random() < .5:
            # first player won
            reportMatch(playerPair[0], playerPair[2])
            print 'Winner: {0}\tLoser: {1}'.format(playerPair[1], playerPair[3])

        else:
            # second player won
            reportMatch(playerPair[2], playerPair[0])
            print 'Winner: {0}\tLoser: {1}'.format(playerPair[3], playerPair[1])

    standings = playerStandings()


