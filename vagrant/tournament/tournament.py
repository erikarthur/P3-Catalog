#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


class Tournament:

    def __init__(self):
        self.i = 1

    def deleteMatches(self, db):
        """Remove all the match records from the database."""
        cur = db.cursor()
        cur.execute("DELETE from matches")
        cur.execute("DELETE from standings")
        db.commit()

    def connect(self):
        """Connect to the PostgreSQL database.  Returns a
        database connection."""
        self.db = psycopg2.connect("dbname='tournament'")
        return self.db

    def deletePlayers(self, db):
        """Remove all the player records from the database."""
        cur = db.cursor()
        cur.execute("DELETE from players;")
        db.commit()

    def countPlayers(self, db):
        """Returns the number of players currently registered."""
        cur = db.cursor()
        cur.execute("select count(name) from players")
        rows = cur.fetchall()
        count = 0
        for row in rows:
            count += row[0]
        return count

    def registerPlayer(self, name, db):
        """Adds a player to the tournament database.

        The database assigns a unique serial id number for the player.  (This
        should be handled by your SQL database schema, not in your Python code.)

        Args:
          name: the player's full name (need not be unique).
        """
        cur = db.cursor()
        cur.execute('INSERT INTO players VALUES (default, %s);', (name,))
        cur.execute('select * from players where name = %s', (name,))
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO standings VALUES (default, %s, %s);', (row[0],0,))
        db.commit()

    def playerStandings(self, db):
        """Returns a list of the players and their win records, sorted by wins.

        The first entry in the list should be the player in first place, or a player
        tied for first place if there is currently a tie.

        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
        """
        print "\n\nCurrent Tournament Standings\n"
        print 'Rank\tName\tPoints'
        cur = db.cursor()
        cur.execute("""select name, points, random() as seed from standings,
                    players where players."ID" = standings."ID"
                    order by points desc, seed desc;""")
        rows = cur.fetchall()
        rank = 1
        for row in rows:
            print '{0}\t{1}\t{2}'.format(rank, row[0], row[1])
            rank = rank + 1
        print

    def reportMatch(self, winner, loser):
        """Records the outcome of a single match between two players.

        Args:
          winner:  the id number of the player who won
          loser:  the id number of the player who lost
        """


    def swissPairings(self, db):
        """Returns a list of pairs of players for the next round of a match.

        Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """


