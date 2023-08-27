CREATE DATABASE PlantsDB;
USE PlantsDB;

CREATE TABLE users (
  user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  firstname VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  passwd VARCHAR(255) NOT NULL
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




