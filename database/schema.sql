-- schema.sql
CREATE DATABASE IF NOT EXISTS image_comparison_db;
USE image_comparison_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comparison_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    image1_path VARCHAR(255) NOT NULL,
    image2_path VARCHAR(255) NOT NULL,
    similarity_value FLOAT NOT NULL,
    compared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);