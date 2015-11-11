from flask import Flask, jsonify, json, Response
import psycopg2
import random
import contextlib
import json
import requests

# import sys
# sys.path.append('pycharm-debug.egg')
#
# import pydevd

app = Flask(__name__)

def connect():
    """Connect to the PostgreSQL database.  Returns a
    database connection."""
    db = psycopg2.connect("dbname=catalog user=erik "
                          "password=erik host=localhost")
    return db

@contextlib.contextmanager
def get_cursor():
    """
    Helper function for using cursors.  Helps to avoid a lot of connect,
    execute, commit code
    """
    conn = connect()
    cur = conn.cursor()
    try:
        yield cur
    except:
        raise
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/categories')
def get_all_categories():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute("select * from categories order by category asc;")
        rows = cursor.fetchall()

        items_list = []

        for item in rows:
            datum = {'id': item[0], 'category': item[1]}
            items_list.append(datum)

        j = json.dumps(items_list)

        return Response(j, status=200, mimetype="application/json")

@app.route('/category/<category>')
def get_category(category):
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute('select * from categories where category = %s '
                       'order by category asc;', (category, ))
        rows = cursor.fetchall()

        items_list = []

        if rows:
            cursor.execute('select *  from items where category = %s',
                           (rows[0][0],))
            items = cursor.fetchall()

            for item in items:
                list_item = {'id': item[0], 'category': item[1],
                         'item_name': item[3],'item_description': item[4],
                         'item_picture' : item[5]}
                items_list.append(list_item)

            j = json.dumps(items_list)

            return Response(j, status=200, mimetype="application/json")
        else:
            return Response(items_list, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.secret_key = 'm-Ho83cJFux7J3XOJPfoz2IP'
    app.debug = True
    app.run(host='0.0.0.0', port=7000)
