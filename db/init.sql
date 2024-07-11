CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');
INSERT INTO users (username, password) VALUES ('user1', 'password1');
