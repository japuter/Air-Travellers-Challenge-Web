import time
from flask import Flask, request, render_template, redirect, url_for, make_response, Blueprint
# from database.db_models import verify_user

games = Blueprint('game', __name__)

# Create a Flask web application
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Define a route and a function to handle requests to the root URL
# 
@games.route('/new-game', methods=['GET'])
def new_game():
    if request.cookies.get('logged_in') == 'yes':
        username = request.cookies.get('username')
        response = make_response(render_template('new-game.html', user=username))    
        return response
    else:
        return make_response(url_for('auth.login'))
        

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)

