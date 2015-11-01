__author__ = 'erik'

from tournament import Tournament

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

t.playerStandings(db)

# t.deletePlayers(db)
print(count)