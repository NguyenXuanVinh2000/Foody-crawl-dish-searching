CREATE DATABASE IF NOT EXISTS FOODY;
USE FOODY;
CREATE TABLE IF NOT EXISTS store (drink_names   longtext CHARSET utf8, prices int, statuss  longtext CHARSET utf8, ratings varchar(3), store_names longtext CHARSET utf8, address longtext CHARSET utf8);