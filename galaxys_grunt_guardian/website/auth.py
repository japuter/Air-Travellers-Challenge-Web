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
    elif request.method == 'POST':
        email = request.form.get('email')
        username =request.form.get('username')
        password = request.form.get('password')

        #  QUERY THE FIRST USER FROM DB BASED ON SUBMIT EMAIL
        user = Player.query.filter_by(email=email).first()
        print(user.password)
        # IF A EMAIL FOR USER IS FOUND
        if user:
            if check_password_hash(user.password, password):
                response = make_response(render_template('success_login.html', user=email))    
                response.set_cookie('logged_in', 'yes')
                return response
            else:
                return render_template('failed_login.html', user=username, message='Incorrect password')
        else:
            return render_template('failed_login.html', user=username, message='Email does not exist')

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

        user = Player.query.filter_by(email=email).first()
        if user:
            return redirect(url_for(auth.login))    
        elif len(email) < 7:
            return redirect(url_for(auth.login))    
        elif len(username) < 3:
            return redirect(url_for(auth.login))    
        elif len(password) < 5:
            return redirect(url_for(auth.login))    
        else:
            new_player = Player(email=email, name=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_player)
            db.session.commit()
            flash('Account created', category='success')
            response = make_response(render_template('success_login.html', user=username))    
            response.set_cookie('logged_in', 'yes')
            return response
            