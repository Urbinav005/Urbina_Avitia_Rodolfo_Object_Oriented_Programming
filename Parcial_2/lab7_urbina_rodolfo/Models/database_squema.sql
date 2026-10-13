CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password varchar (256) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTo users (username, password, nombre) VALUES ('admin','admin123')