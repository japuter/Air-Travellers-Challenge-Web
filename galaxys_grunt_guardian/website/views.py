import time
from flask import Flask, request, render_template, redirect, url_for, make_response, Blueprint

views = Blueprint('views', __name__)

# Create a Flask web application
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Define a route and a function to handle requests to the root URL
@views.route('/')
def index():
    if request.cookies.get('logged_in') == 'yes':
        return render_template('main_menu.html') #IF USER HAS LOGIN COOKIES, LOAD MAIN MENU PAGE
    else:
        return redirect(url_for('auth.login')) # IF USER HAS NO LOGIN COOKIES REDIRECT TO LOGIN PAGE



# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)

