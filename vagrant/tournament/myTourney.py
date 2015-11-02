__author__ = 'erik'

from tournament import Tournament
import math

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
    print x
    t.playerStandings(db)
    results = t.swissPairings(db)


