import time
from flask import Flask, request, render_template, redirect, url_for, make_response
from database.db_models import verify_user

# Create a Flask web application
app = Flask(__name__, static_url_path='/static', static_folder='static')

users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Define a route and a function to handle requests to the root URL
@app.route('/')
def index():
    if request.cookies.get('logged_in') == 'yes':
        return render_template('index.html') #IF USER HAS LOGIN COOKIES, LOAD MAIN MENU PAGE
    else:
        return redirect(url_for('login')) # IF USER HAS NO LOGIN COOKIES REDIRECT TO LOGIN PAGE

# ROUTE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in based on a cookie
    if request.cookies.get('logged_in') == 'yes':
        return redirect(url_for('index'))  # Redirect to the homepage

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        logged_in = verify_user(username, password)

        if logged_in:
            # Set a cookie to indicate that the user is logged in
            response = make_response(render_template('success_login.html'))    
            response.set_cookie('logged_in', 'yes')
            return response
        else:
            return 'Login failed. Please check your username and password.'
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    # Clear the "logged_in" cookie to log the user out
    if request.cookies.get('logged_in') == 'yes':
        response = make_response(render_template('logout.html'))
        response.set_cookie('logged_in', '', expires=0)  # Set the cookie to expire immediately
        return response
    
@app.route('/signup', methods=['POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('signup_email')
        username = request.form.get('signup_username')
        password = request.form.get('signup_password')

        if username not in users and users[username] == password:
            # Set a cookie to indicate that the user is logged in
            response = make_response(render_template('success_login.html'))    
            response.set_cookie('logged_in', 'yes')
            return response
        else:
            return 'Login failed. Please check your username and password.'

@app.route('/new-game', methods=['GET'])
def new_game():
    pass



# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
