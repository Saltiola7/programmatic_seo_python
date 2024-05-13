CREATE TABLE rent_car_brand_model_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Rent ', car_brand, ' ', car_model, ' in ', city))
);

CREATE TABLE rent_car_brand_model_for_holiday (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    holiday VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Rent ', car_brand, ' ', car_model, ' for ', holiday))
);

CREATE TABLE special_weekend_offer_rent_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Special weekend offer: Rent ', car_brand, ' ', car_model, ' in ', city))
);

CREATE TABLE rent_for_holiday_with_discount (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    holiday VARCHAR(255),
    discount VARCHAR(50),
    completed_structure VARCHAR(255) AS (CONCAT('Rent ', car_brand, ' ', car_model, ' for ', holiday, ' with a ', discount, ' discount'))
);

CREATE TABLE book_business_trip_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Book a business trip in ', city, ' with a ', car_brand, ' ', car_model))
);

CREATE TABLE experience_luxury_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Experience luxury in ', city, ': Rent a ', car_brand, ' ', car_model))
);

CREATE TABLE family_package_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Family package in ', city, ': Rent a spacious ', car_brand, ' ', car_model))
);

CREATE TABLE group_discount_for_trip_to_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Group discount available: Rent ', car_brand, ' ', car_model, ' for your trip to ', city))
);

CREATE TABLE go_green_in_city_with_eco_friendly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Go green in ', city, ' with our eco-friendly ', car_brand, ' ', car_model))
);

CREATE TABLE rent_electric_explore_city_sustainably (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Rent an electric ', car_brand, ' ', car_model, ' and explore ', city, ' sustainably'))
);

CREATE TABLE rent_for_snowy_holiday_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    holiday VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Rent ', car_brand, ' ', car_model, ' for a snowy ', holiday, ' in ', city))
);

CREATE TABLE summer_adventures_in_city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Summer adventures in ', city, ': Rent a ', car_brand, ' ', car_model, ' for your vacation'))
);

CREATE TABLE enjoy_event_in_city_with_car (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_brand VARCHAR(255),
    car_model VARCHAR(255),
    event VARCHAR(255),
    city VARCHAR(255),
    completed_structure VARCHAR(255) AS (CONCAT('Enjoy ', event, ' in ', city, ' with a ', car_brand, ' ', car_model))
);