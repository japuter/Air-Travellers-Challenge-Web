from . import db 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum('lava', 'ice', 'jungle', 'desert'), nullable=False)
    description = Column(String(255))
    planet_url = Column(String(255))
    min_player_level = Column(Integer, nullable=False)
    enemy_waves = Column(Integer, nullable=False)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    password = Column(String(150), nullable=False)
    level = Column(Integer, nullable=False, default=1)
    xp = Column(Integer, nullable=False, default=0)
    # location_id = Column(Integer, ForeignKey('planets.id'))
    
    # Define the relationship, this will add a 'players' attribute to the Planet class
    location = relationship("Planet", backref="players")

class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    xp = Column(Integer, nullable=False, default=0)
    health = Column(Integer, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))

    # Define the relationship, this will add a 'game' attribute to the Player class
    player = relationship("Player", backref="games")

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///ggg.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

    
