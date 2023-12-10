-- Crear una Base de Datos, el usuario y contraseña.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crear el usuario user_0d_2 y otorgar privilegio SELECT en la base de datos hbtn_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
