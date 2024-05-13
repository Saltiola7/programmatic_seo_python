-- Insert data into cities
INSERT INTO cities (name) VALUES ('Helsinki');
INSERT INTO cities (name) VALUES ('Espoo');
INSERT INTO cities (name) VALUES ('Tampere');

-- Insert data into suburbs
INSERT INTO suburbs (name, city_id) VALUES ('Kallio', 1);
INSERT INTO suburbs (name, city_id) VALUES ('Otaniemi', 2);
INSERT INTO suburbs (name, city_id) VALUES ('Hervanta', 3);

-- Insert data into car_brands
INSERT INTO car_brands (name) VALUES ('Toyota');
INSERT INTO car_brands (name) VALUES ('Tesla');
INSERT INTO car_brands (name) VALUES ('Ford');

-- Insert data into car_models
INSERT INTO car_models (name, brand_id) VALUES ('Corolla', 1);
INSERT INTO car_models (name, brand_id) VALUES ('Model S', 2);
INSERT INTO car_models (name, brand_id) VALUES ('Fiesta', 3);

-- Insert data into holiday_seasons
INSERT INTO holiday_seasons (name, description) VALUES ('Christmas', 'Special rates for Christmas season');
INSERT INTO holiday_seasons (name, description) VALUES ('Midsummer', 'Enjoy the longest day of the year with a scenic drive');

-- Insert data into special_offers
INSERT INTO special_offers (description, validity) VALUES ('20% off on all SUV rentals', '2023-12-31');
INSERT INTO special_offers (description, validity) VALUES ('Free additional driver with every booking', '2023-06-30');