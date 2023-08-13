DROP DATABASE IF EXISTS PlantsDB;
CREATE DATABASE PlantsDB;
USE PlantsDB;

CREATE TABLE users (
  user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  firstname VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
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

-- To display the plant collection of each user as well as upcoming care action.
SELECT 
    u.user_id, 
    u.email,
    (
        SELECT CONCAT('[', GROUP_CONCAT(JSON_OBJECT('common_name', p.common_name, 'upcoming_care', pc.upcoming_care)), ']')
        FROM plant_collection pc INNER JOIN
        plants p ON pc.plant_id = p.plant_id
        WHERE pc.user_id = u.user_id
    ) AS plants
FROM users u;

select * from users;
insert into plant_collection
(user_id, plant_id, last_care, upcoming_care)
values
(1, 1, null, null),
(1, 2, null, null);

select * from plant_collection;
select * from plants;

# get list of plants in user collection
SELECT pc.plant_id, p.common_name, p.scientific_name, pc.upcoming_care, p.image FROM plant_collection pc
LEFT JOIN plants p 
ON p.plant_id = pc.plant_id
WHERE user_id = 1;






