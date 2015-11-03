#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    tournament_cursor = db.cursor()
    tournament_cursor.execute("DELETE from matches")
    tournament_cursor.execute("DELETE from standings")
    db.commit()
    db.close()


def connect():
    """Connect to the PostgreSQL database.  Returns a
    database connection."""
    db = psycopg2.connect("dbname='tournament'")
    return db


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()

    tournament_cursor = db.cursor()
    tournament_cursor.execute("DELETE from players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    tournament_cursor = db.cursor()
    tournament_cursor.execute("select count(name) from players")
    rows = tournament_cursor.fetchall()
    count = 0
    [count] = [row[0] for row in rows]
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    tournament_cursor = db.cursor()
    tournament_cursor.execute('INSERT INTO players VALUES (default, %s);', (name,))
    tournament_cursor.execute('select * from players where name = %s', (name,))
    rows = tournament_cursor.fetchall()
    for row in rows:
        tournament_cursor.execute('INSERT INTO standings VALUES (default, %s, %s, %s, %s);', (row[0], 0, 0, 0))
    db.commit()
    db.close()


def playerStandings():
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
    db = connect()
    print "\nCurrent Tournament Standings\n"
    print 'Rank\tName\tPoints'
    tournament_cursor = db.cursor()
    tournament_cursor.execute(
        "select players.id, name, wins, matches from standings, players "
        "where players.id = standings.id order by wins desc, name asc;")

    rows = tournament_cursor.fetchall()

    # close connection
    db.close()

    # create local variable for calculating rank
    rank = 0
    currentWins = -1

    # output list
    currentStandings = []

    for row in rows:
        # check each players wins against wins from prior players.
        # increment rank if necessary
        if currentWins != row[2]:
            rank = rank + 1
            currentWins = row[2]

        # add tuple standings list
        currentStandings.append((row[0], row[1], row[2], row[3]))
        print '{0}\t{1}\t{2}'.format(rank, row[1], row[2])
        # rank = rank + 1
    print '\n-----------------------------\n'

    #return results
    return currentStandings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    tournament_cursor = db.cursor()
    tournament_cursor.execute(
        'insert into matches values (default, %s, %s);', (winner, loser,))
    tournament_cursor.execute(
        'update standings set matches = matches + 1, wins = wins + 1  '
        'where player_id = %s;', (winner,))
    tournament_cursor.execute(
        'update standings set matches = matches + 1, losses = losses + 1 '
        'where player_id = %s;', (loser,))
    db.commit()
    db.close()


def swissPairings():
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
    db = connect()
    tournament_cursor = db.cursor()

    tournament_cursor.execute(
        'select players.id, name, wins, random() as seed from standings, '
        'players where players.id = standings.id order by wins desc, '
        'seed desc;')

    rows = tournament_cursor.fetchall()
    db.close()

    results = []
    for x in xrange(0, len(rows), 2):
        results.append((rows[x][0], rows[x][1], rows[x+1][0], rows[x+1][1]))

    return results



