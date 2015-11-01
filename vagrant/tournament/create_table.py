#!/usr/bin/python

import psycopg2
from pydev import pydevd

pydevd.settrace('localhost', port=$SERVER_PORT, stdoutToServer=True, stderrToServer=True)

conn = psycopg2.connect(database="tournament")

print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully"

conn.commit()
conn.close()
