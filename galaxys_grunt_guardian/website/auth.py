import time
from flask import Flask, flash, request, render_template, redirect, url_for, make_response, Blueprint
from .models import Player
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# ROUTE LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in based on a cookie
    if request.cookies.get('logged_in') == 'yes':
        return render_template('main_menu.html')  # Redirect to the homepage

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # logged_in = verify_user(username, password)

        # if logged_in:
            # Set a cookie to indicate that the user is logged in
        response = make_response(render_template('success_login.html', user=logged_in))    
        response.set_cookie('logged_in', 'yes')
        return response
        # else:
        #     return 'Login failed. Please check your username and password.'
    else:
        return render_template('login.html')


@auth.route('/logout', methods=['GET'])
def logout():
    # Clear the "logged_in" cookie to log the user out
    if request.cookies.get('logged_in') == 'yes':
        response = make_response(render_template('logout.html'))
        response.set_cookie('logged_in', '', expires=0)  # Set the cookie to expire immediately
        return response
    else:
        response = make_response(render_template('login.html'))
        return response
    
@auth.route('/signup', methods=['POST'])
def signup():

    if request.method == 'GET':
        return redirect(url_for(auth.login))
    elif request.method == 'POST':
        email = request.form.get('signup_email')
        username = request.form.get('signup_username')
        password = request.form.get('signup_password')

        if len(email) < 10:
            flash('Email must be greater than 10 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(password) < 5:
            flash('Username must be greater than 5 characters.', category='error')
        else:
            new_player = Player(name=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_player)
            db.session.commit()
            flash('Account created', category='success')
            response = make_response(render_template('success_login.html', user=username))    
            response.set_cookie('logged_in', 'yes')
            return response
            