CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
CREATE USER 'admin'@'%' IDENTIFIED BY 'admin123';

DROP DATABASE IF EXISTS `pysite`;
CREATE DATABASE `pysite`;

GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL ON *.* TO 'admin'@'%' IDENTIFIED BY 'admin123';
FLUSH PRIVILEGES;

USE pysite;

DROP TABLE IF EXISTS `users`;
CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    cola INT DEFAULT 0,
    water INT DEFAULT 0,
    fanta INT DEFAULT 0
);