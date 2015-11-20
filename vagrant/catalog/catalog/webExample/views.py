from flask import render_template
from flask import session as login_session
from webExample import app
from webExample import db
from webExample import Owners, Categories, Items
import random
import string


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

@app.route('/')
def index():
    categories = db.session.query(Categories).order_by(Categories.category_name).all()
    latest_items = db.session.query(Items).order_by(Items.insert_date.desc()).limit(10)
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    # login_session['state'] = state

    if login_session.get('email'):
        email = login_session['email']
    else:
        email = False

    return render_template(
        "pages/latest-items.html", categories=categories,
        latest_items=latest_items,
        home='/', STATE=state, email=email)


@app.route('/category/<name>')
def get_category_items(name):

    categories = db.session.query(Categories).order_by(Categories.category_name).all()
    categoryFilter = db.session.query(Categories).filter_by(category_name=name).first()
    category = db.session.query(Items).filter_by(category=categoryFilter).all()

    return render_template(
        "pages/item-page.html", categories=categories, category=category,
        name=name, server='/category/',
        home='/')


# @app.route('/add-category', methods=['GET', 'POST'])
# def add_category():
#
#     if login_session['email']:
#         form = Category(request.form)
#
#         if request.method == 'POST' and form.validate():
#             # add data
#             with get_cursor() as cursor:
#                 cursor.execute(
#                     'select owner_id from owners where owner_email = %s;',
#                     (login_session['email'],))
#                 print login_session['email']
#                 output = cursor.fetchall()
#                 user_id = output[0][0]
#
#                 cate = form.data['category_name']
#                 cursor.execute(
#                     'INSERT INTO categories VALUES (default, %s, %s, now());',
#                     (cate,user_id,))
#             return redirect( url_for('hello_world') )
#         return render_template('pages/add-category.html', form=form)