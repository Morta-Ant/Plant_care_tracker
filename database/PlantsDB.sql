CREATE DATABASE PlantsDB;
USE PlantsDB;

CREATE TABLE users (
  user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE plants (
  plant_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  common_name VARCHAR(255) NOT NULL,
  scientific_name VARCHAR(255),
  other_name VARCHAR(255),
  watering_frequency INTEGER,
  growth_rate VARCHAR(255),
  light_level VARCHAR(255),
  maintenance_level VARCHAR(255),
  plant_description VARCHAR(255),
  image VARCHAR(255)
);

CREATE TABLE plant_collection (
  user_id INTEGER NOT NULL,
  plant_id INTEGER NOT NULL,
  last_care DATETIME,
  upcoming_care DATETIME,
  PRIMARY KEY (user_id, plant_id)
);

ALTER TABLE plant_collection ADD FOREIGN KEY (plant_id) REFERENCES plants (plant_id);
ALTER TABLE plant_collection ADD FOREIGN KEY (user_id) REFERENCES users (user_id);

-- To display the plant collection of each user as well as upcoming care action.
SELECT 
    u.user_id, 
    u.username,
    u.email,
    (
        SELECT CONCAT('[', GROUP_CONCAT(JSON_OBJECT('common_name', p.common_name, 'upcoming_care', pc.upcoming_care)), ']')
        FROM plant_collection pc INNER JOIN
        plants p ON pc.plant_id = p.plant_id
        WHERE pc.user_id = u.user_id
    ) AS plants
FROM users u;
