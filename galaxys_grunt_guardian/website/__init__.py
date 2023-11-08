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

    from .models import Planet, Player, Game

    create_database(app)

    return app

def create_database(app):
    if not path.exists('./' + DB_NAME):
        with app.app_context():
            try:
                db.create_all()
                print('Created database!')
                
                from .models import Planet

                # ADD ALL THE PLANETS TO DATABASE
                planet_details = [
                {'type': 'lava', 'description': 'A hot and fiery planet.', 'planet_url': 'http://example.com/lava', 'min_player_level': 5, 'enemy_waves': 3},
                {'type': 'ice', 'description': 'A cold and icy planet.', 'planet_url': 'http://example.com/ice', 'min_player_level': 3, 'enemy_waves': 5},
                {'type': 'jungle', 'description': 'A lush and dangerous jungle planet.', 'planet_url': 'http://example.com/jungle', 'min_player_level': 8, 'enemy_waves': 4},
                {'type': 'desert', 'description': 'A vast and scorching desert planet.', 'planet_url': 'http://example.com/desert', 'min_player_level': 2, 'enemy_waves': 2},
                ]
                planets = [Planet(**details) for details in planet_details]

                # Add all the new Planet instances to the session
                db.session.add_all(planets)

                # Commit the session to save the planets to the database
                try:
                    db.session.commit()
                    print("Planets have been added to the database.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    db.session.rollback()
            except Exception as e:
                logging.exception('An error occurred when creating database!')

                print('An error occurred when creating database!', e)