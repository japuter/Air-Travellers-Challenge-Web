     
                                    
                _________      .__    ___________      __________              
               /   _____/ _____|  |   \__    ___/___   \______   \__ __  ____  
               \_____  \ / ____/  |     |    | /  _ \   |       _/  |  \/    \ 
               /        < <_|  |  |__   |    |(  <_> )  |    |   \  |  /   |  \
              /_______  /\__   |____/   |____| \____/   |____|_  /____/|___|  /
                      \/    |__|                               \/           \/ 

```markdown
# SQL Database Setup

In this section, we'll provide instructions for setting up the flight_game database and making necessary schema changes. 

## Download the flight_game Database

To get started, download the flight_game database using the following link:
[Download flight_game Database]
https://moodle2.metropolia.fi/pluginfile.php/1561494/mod_resource/content/1/lp.sql

## MySQL Console Commands

After downloading the database, run the following MySQL commands in your console to make the required modifications:

```sql

CREATE DATABASE ggg;

use ggg;

-- PLANETS table
CREATE TABLE PLANETS (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    type SET('lava', 'ice', 'jungle', 'desert') NOT NULL,
    description VARCHAR(255),
    planet_url VARCHAR(255),
    min_player_level INT NOT NULL,
    enemy_waves INT NOT NULL
);

-- PLAYERS table
CREATE TABLE PLAYERS (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
    level INT NOT NULL DEFAULT 1,
    xp INT NOT NULL DEFAULT 0,
    location_id INT, -- FK to PLANETS
    FOREIGN KEY (location_id) REFERENCES PLANETS(id)
);

-- GAME table
CREATE TABLE GAME (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    level INT NOT NULL,
    xp INT NOT NULL DEFAULT 0,
    health INT NOT NULL,
    player_id INT, -- FK to PLAYERS
    FOREIGN KEY (player_id) REFERENCES PLAYERS(id)
);

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('desert', 'Sandy dunes, scarce water sources, and ancient ruins. Sandstorms limit visibility and slow movement, while quicksand pits trap enemies.', 1, 3, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_desert.png');

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('ice', 'Frigid climate with ice structures and frequent snowfall. Slippery terrain affects movement, and icicles can be shot to fall on enemies.', 1, 3, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_ice_1.png');

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('ice', 'Frigid climate with ice structures and frequent snowfall. Slippery terrain affects movement, and icicles can be shot to fall on enemies.', 2, 3, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_ice_2.png');

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('jungle', 'Dense forests, vibrant flora, teeming with wildlife. Thick foliage hides enemies or power-ups, with some areas inaccessible until cleared.', 3, 5, /* Specify planet_url for Jungle Planet here */);

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('ice', 'Frigid climate with ice structures and frequent snowfall. Slippery terrain affects movement, and icicles can be shot to fall on enemies.', 3, 5, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_jungle_1.png');

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('lava', 'Fiery environment with rivers of lava and volcanic eruptions. Periodic eruptions send waves of lava or fireballs across the play area.', 5, 10, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_lava_1.png');

INSERT INTO PLANETS (type, description, min_player_level, enemy_waves, planet_url) VALUES 
('ice', 'Frigid climate with ice structures and frequent snowfall. Slippery terrain affects movement, and icicles can be shot to fall on enemies.', 5, 10, 'https://users.metropolia.fi/~konstalk/images/PLANETS/planet_jungle_1.png');




INSERT INTO PLAYERS (name, password, location_id) VALUES ('Konsta', 'test', 1)

## Database Schema Diagram

Below is a database schema diagram for reference:

![Database Schema](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/images/ER_V2.png)

