from flask import Flask, render_template, json
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get('http://192.168.103.217:7000/categories')
    j = r.json()
    return render_template("temp.html", rows=j, server='http://192.168.103.217:7000/category/')

@app.route('/test')
def hello_world2():
    return "Hello World"


if __name__ == '__main__':
    app.secret_key = 'm-Ho83cJFux7J3XOJPfoz2IP'
    app.debug = True
    app.run(host='0.0.0.0', port=8001)
    app.run()