from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import logging

db = SQLAlchemy()
DB_NAME = "ggg.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MAAILMAN SALAISIN SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///../{DB_NAME}'
    
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .games import games

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(games, url_prefix='/game/')

    # from .models import Planet, Player, Game
    from .models import Player

    create_database(app)

    return app

def create_database(app):
    if not path.exists('./' + DB_NAME):
        with app.app_context():
            try:
                db.create_all()
                print('Created database!')
            except Exception as e:
                logging.exception('An error occurred when creating database!')

                print('An error occurred when creating database!', e)