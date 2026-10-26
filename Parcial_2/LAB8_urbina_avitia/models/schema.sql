-- Ejecutar en MySQL antes de iniciar la aplicación:
--   mysql -u root -p < models/schema.sql
CREATE DATABASE IF NOT EXISTS lab8_login;

USE lab8_login;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
