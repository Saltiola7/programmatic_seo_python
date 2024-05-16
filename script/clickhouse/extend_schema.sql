CREATE TABLE price_ranges (
    price_range_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL, -- e.g., "under $100"
    upper_limit INTEGER, -- e.g., 100 for "under $100"
    lower_limit INTEGER -- e.g., 0, could be used for ranges like "$50 to $100"
);

CREATE TABLE car_types (
    car_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL -- e.g., sedan, SUV
);

CREATE TABLE mileage_ranges (
    mileage_range_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL, -- e.g., "0-10000 miles"
    upper_limit INTEGER,
    lower_limit INTEGER
);

CREATE TABLE car_features (
    car_id INTEGER,
    feature_id INTEGER,
    PRIMARY KEY (car_id, feature_id),
    FOREIGN KEY (car_id) REFERENCES car_models(model_id),
    FOREIGN KEY (feature_id) REFERENCES features(feature_id)
);

CREATE TABLE car_rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    car_id INTEGER,
    price_range_id INTEGER,
    holiday_season_id INTEGER,
    special_offer_id INTEGER,
    -- Assume IDs for car_type, transmission_type, etc., as foreign keys
    mileage_range_id INTEGER,
    -- Additional attributes as needed
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    FOREIGN KEY (car_id) REFERENCES car_models(model_id),
    FOREIGN KEY (price_range_id) REFERENCES price_ranges(price_range_id),
    FOREIGN KEY (holiday_season_id) REFERENCES holiday_seasons(season_id),
    FOREIGN KEY (special_offer_id) REFERENCES special_offers(offer_id),
    FOREIGN KEY (mileage_range_id) REFERENCES mileage_ranges(mileage_range_id)
    -- Add more FOREIGN KEY constraints as needed
);