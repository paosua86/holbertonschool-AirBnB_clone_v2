-- script that test a MySQL server for the project --
-- Create database --

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create User --

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Setting privileges of User --

GRANT ALL PRIVILEGES ON hbnb_test_db.* to 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
