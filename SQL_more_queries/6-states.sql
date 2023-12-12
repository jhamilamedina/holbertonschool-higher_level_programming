-- Cree la base de datos hbtn_0d_usa y los estados de la tabla (en la base de datos hbtn_0d_usa).
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
