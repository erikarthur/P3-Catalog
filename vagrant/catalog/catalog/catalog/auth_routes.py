from flask import Flask, render_template, json, request, redirect
from flask import jsonify, url_for, flash, make_response
from flask import session as login_session
import requests
import os
from flask import Response
import psycopg2
import random
import contextlib
import json
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json

from catalog import app

cs_file_path = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
CLIENT_ID = json.loads(
    open(cs_file_path, 'r').read())['catalog']['client_id']

@app.route('/gconnect', methods=['POST'])
def post_signin():
    # Validate state token
    # if request.args.get('state') != login_session['state']:
    #     response = make_response(json.dumps('Invalid state parameter.'), 401)
    #     response.headers['Content-Type'] = 'application/json'
    #     return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        cs_file_path = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
        oauth_flow = flow_from_clientsecrets(cs_file_path, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # login_session['user_id'] = data['user_id']

    # see if user exists, if it doesn't make a new one
    # user_id = getUserID(login_session['email'])
    # if not user_id:
    #     user_id = createUser(login_session)
    # login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    return output

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    # if request.args.get('state') != login_session['state']:
    #     response = make_response(json.dumps('Invalid state parameter.'), 401)
    #     response.headers['Content-Type'] = 'application/json'
    #     return response
    access_token = request.data
    print "access token received %s " % access_token

    cs_file_path = os.path.join(os.path.dirname(__file__), 'fb_client_secrets.json')
    app_id = json.loads(open(cs_file_path, 'r').read())[
        'catalog']['app_id']
    app_secret = json.loads(
        open(cs_file_path, 'r').read())['catalog']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # strip expire tag from access token
    token = result.split("&")[0]


    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email,picture' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    # if data["picture"]['data']['url']:
    #     login_session['picture'] = data["picture"]['data']['url']

    # The token must be stored in the login_session in order to properly
    # logout, let's strip out the information before the equals sign in
    # our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=20&width=20' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # # see if user exists
    # # user_id = getUserID(login_session['email'])
    # # if not user_id:
    # #     user_id = createUser(login_session)
    # # login_session['user_id'] = user_id
    # login_session['user_id'] = 'erik'

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 20px; height: 20px;border-radius: 20px;-webkit-border-radius: 20px;-moz-border-radius: 20px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output