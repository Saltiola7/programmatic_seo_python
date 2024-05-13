INSERT INTO price_ranges (description, upper_limit, lower_limit) VALUES ('Under $100', 100, 0);
INSERT INTO price_ranges (description, upper_limit, lower_limit) VALUES ('$100 to $200', 200, 100);

INSERT INTO car_types (type) VALUES ('Sedan');
INSERT INTO car_types (type) VALUES ('SUV');

INSERT INTO mileage_ranges (description, upper_limit, lower_limit) VALUES ('0-10000 miles', 10000, 0);
INSERT INTO mileage_ranges (description, upper_limit, lower_limit) VALUES ('10000-20000 miles', 20000, 10000);

-- Assuming a table structure for features
INSERT INTO features (description) VALUES ('Air conditioning');
INSERT INTO features (description) VALUES ('GPS navigation');

-- Assuming a table structure for amenities
INSERT INTO amenities (description) VALUES ('Free Wi-Fi');
INSERT INTO amenities (description) VALUES ('Roadside assistance');

-- Assuming you have entries in the cities, car_models, price_ranges, holiday_seasons, special_offers, and mileage_ranges tables
INSERT INTO car_rentals (city_id, car_id, price_range_id, holiday_season_id, special_offer_id, mileage_range_id) VALUES (1, 1, 1, 1, 1, 1);
INSERT INTO car_rentals (city_id, car_id, price_range_id, holiday_season_id, special_offer_id, mileage_range_id) VALUES (2, 2, 2, 2, 2, 2);