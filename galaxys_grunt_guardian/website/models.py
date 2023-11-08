# MODELS.PY

from . import db 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship, sessionmaker
from os import path
from flask_login import UserMixin

# FIX DB MODELS TO USE USERMIXIN AND FIGURE OUT WHAT IT IS AND HOW DOES IT DIFFER FROM THE FIRST APPROACH

class Planet(db.Model):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum('lava', 'ice', 'jungle', 'desert'), nullable=False)
    description = Column(String(255))
    planet_url = Column(String(255))
    min_player_level = Column(Integer, nullable=False)
    enemy_waves = Column(Integer, nullable=False)

class Player(db.Model, UserMixin):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(300), nullable=False)
    name = Column(String(150), nullable=False)
    password = Column(String(150), nullable=False)
    level = Column(Integer, nullable=False, default=1)
    xp = Column(Integer, nullable=False, default=0)
    location_id = Column(Integer, ForeignKey('planets.id'))
    
    # Define the relationship, this will add a 'players' attribute to the Planet class
    location = relationship("Planet", backref="players")

class Game(db.Model):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    xp = Column(Integer, nullable=False, default=0)
    health = Column(Integer, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))

    # Define the relationship, this will add a 'game' attribute to the Player class
    player = relationship("Player", backref="game")