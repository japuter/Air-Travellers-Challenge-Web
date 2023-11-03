import time
from flask import Flask, request, render_template, redirect, url_for, make_response

# Create a Flask web application
app = Flask(__name__, static_url_path='/static', static_folder='static')

users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Define a route and a function to handle requests to the root URL
@app.route('/')
def index():
    return render_template('index.html')

# ROUTE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in based on a cookie
    if request.cookies.get('logged_in') == 'yes':
        return redirect(url_for('index'))  # Redirect to the homepage

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            # Set a cookie to indicate that the user is logged in
            response = make_response(render_template('success_login.html'))    
            response.set_cookie('logged_in', 'yes')
            return response
        else:
            return 'Login failed. Please check your username and password.'

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



# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
