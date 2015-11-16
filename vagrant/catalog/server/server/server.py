from flask import Flask, jsonify, json, Response, request
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
    db = psycopg2.connect("dbname=catalog user=postgres "
                          "password=postgres host=localhost")
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
    return 'Catalog server.  Query from front end'

@app.route('/categories')
def get_all_categories():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute("select * from categories order by category asc;")
        rows = cursor.fetchall()

        items_list = []

        for item in rows:
            datum = {'id': item[0], 'category': item[1].replace(" ", "-")}
            items_list.append(datum)

        json_returned = json.dumps(items_list)

        return Response(json_returned, status=200, mimetype="application/json")

@app.route('/latest-items')
def get_latest_items():
     with get_cursor() as cursor:
        cursor.execute("SELECT item_name, item_description, item_picture FROM items order by item_insert_date desc "
                       "limit 10;")
        rows = cursor.fetchall()

        items_list = []

        for item in rows:
            datum = {'name': item[0], 'description': item[1], 'picture' :
                     item[2]}
            items_list.append(datum)

        json_returned = json.dumps(items_list)

        return Response(json_returned, status=200, mimetype="application/json")

@app.route('/category/<category>')
def get_category(category):
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute('select * from category_view where category = %s;',
                       (category, ))
        items = cursor.fetchall()

        items_list = []

        if items:
            for item in items:
                list_item = {'id': item[0], 'category': item[6],
                         'item_name': item[1], 'item_description': item[2],
                         'item_picture': item[3], 'owner': item[5],
                         'email': item[4]}
                items_list.append(list_item)

            json_returned = json.dumps(items_list)

            return Response(json_returned, status=200, mimetype="application/json")
        else:
            return Response(items_list, status=200, mimetype="application/json")

@app.route('/addcategory', methods=['POST'])
def add_category():
    if app.secret_key == request.form['secret']:
        owner_id = request.form['owner_id']
        category = request.form['category']
        with get_cursor() as cursor:
            cursor.execute('INSERT INTO categories(id, owner_id, category) '
                           'VALUES (default, %s, %s);', (owner_id, category, ))

            return Response(None, status=200, mimetype="application/json")
    else:
        return Response(None, status=201, mimetype="application/json")

if __name__ == '__main__':
    app.secret_key = 'm-Ho83cJFux7J3XOJPfoz2IP'
    app.debug = True
    app.run(host='0.0.0.0', port=7000)
