CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

-- Tabla de usuarios (la que usa el login)
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id_user    INT AUTO_INCREMENT PRIMARY KEY,
    username   VARCHAR(50)  NOT NULL UNIQUE,
    passw      VARCHAR(256) NOT NULL,
    nombre     VARCHAR(50)  NOT NULL,
    email      VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, passw, nombre, email)
VALUES ('admin', 'admin123', 'Administrador', 'admin@example.com');

-- Tabla de productos (tema: tienda de videojuegos)
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100)   NOT NULL,
    precio     DECIMAL(10, 2) NOT NULL,
    stock      INT            NOT NULL
);

INSERT INTO products (nombre, precio, stock) VALUES
('Control inalámbrico Pro', 1299.00, 20),
('Auriculares gamer 7.1', 1599.00, 15),
('Teclado mecánico RGB', 1799.00, 12),
('Mouse gamer 16000 DPI', 899.00, 25),
('Tarjeta de regalo $500', 500.00, 50);