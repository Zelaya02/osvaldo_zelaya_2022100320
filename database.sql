CREATE DATABASE IF NOT EXISTS ganaderia_db;
USE ganaderia_db;


CREATE TABLE IF NOT EXISTS contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    horario_llamada VARCHAR(50) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS ganado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria ENUM('ternero', 'novillo', 'novillito', 'vaquillona', 'vaca', 'toro') NOT NULL,
    lote VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    imagen VARCHAR(255),
    descripcion TEXT
);


INSERT INTO ganado (categoria, lote, cantidad, precio, imagen, descripcion) VALUES
('ternero', 'Lote A', 25, 450000.00, 'ternero.jpg', 'Terneros de 6-8 meses'),
('novillo', 'Lote B', 18, 1200000.00, 'novillo.jpg', 'Novillos de 18-24 meses'),
('novillito', 'Lote C', 32, 800000.00, 'novillito.jpg', 'Novillitos de 12-16 meses'),
('vaquillona', 'Lote D', 15, 1500000.00, 'vaquillona.jpg', 'Vaquillonas para reposición'),
('vaca', 'Lote E', 22, 1800000.00, 'vaca.jpg', 'Vacas preñadas'),
('toro', 'Lote F', 8, 2500000.00, 'toro.jpg', 'Toros reproductores');