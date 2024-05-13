-- Cities where the car rental service operates
CREATE TABLE cities (
    city_id UInt32,
    name String,
    PRIMARY KEY (city_id)
) ENGINE = MergeTree ORDER BY city_id;

-- Suburbs within the cities for more granular targeting
CREATE TABLE suburbs (
    suburb_id UInt32,
    name String,
    city_id UInt32,
    PRIMARY KEY (suburb_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
) ENGINE = MergeTree ORDER BY suburb_id;

-- Car brands available for rental
CREATE TABLE car_brands (
    brand_id UInt32,
    name String,
    PRIMARY KEY (brand_id)
) ENGINE = MergeTree ORDER BY brand_id;

-- Specific models of cars available under each brand
CREATE TABLE car_models (
    model_id UInt32,
    name String,
    brand_id UInt32,
    PRIMARY KEY (model_id),
    FOREIGN KEY (brand_id) REFERENCES car_brands(brand_id)
) ENGINE = MergeTree ORDER BY model_id;

-- Templates for generating SEO-friendly content
CREATE TABLE programmatic_structures (
    id UInt32,
    structure String,
    description String,
    PRIMARY KEY (id)
) ENGINE = MergeTree ORDER BY id;

-- Defines various holiday seasons to target specific campaigns
CREATE TABLE holiday_seasons (
    season_id UInt32,
    name String NOT NULL,
    description String,
    PRIMARY KEY (season_id)
) ENGINE = MergeTree ORDER BY season_id;

-- Special offers available for a limited time
CREATE TABLE special_offers (
    offer_id UInt32,
    description String,
    validity Date,
    PRIMARY KEY (offer_id)
) ENGINE = MergeTree ORDER BY offer_id;

-- Price ranges for rentals to target different customer segments
CREATE TABLE price_ranges (
    price_range_id UInt32,
    description String,
    PRIMARY KEY (price_range_id)
) ENGINE = MergeTree ORDER BY price_range_id;

-- Types of cars (e.g., SUV, sedan, electric) for more detailed targeting
CREATE TABLE car_types (
    car_type_id UInt32,
    type_name String,
    PRIMARY KEY (car_type_id)
) ENGINE = MergeTree ORDER BY car_type_id;

-- Features of cars (e.g., GPS, air conditioning) to highlight in listings
CREATE TABLE car_features (
    feature_id UInt32,
    feature_name String,
    PRIMARY KEY (feature_id)
) ENGINE = MergeTree ORDER BY feature_id;

-- Mileage ranges for electric vehicles or to highlight fuel efficiency
CREATE TABLE mileage_ranges (
    mileage_range_id UInt32,
    description String,
    PRIMARY KEY (mileage_range_id)
) ENGINE = MergeTree ORDER BY mileage_range_id;

CREATE TABLE schema_org_templates (
    template_id INTEGER PRIMARY KEY,
    template_name TEXT NOT NULL,
    markup_template TEXT NOT NULL,
    description TEXT
);

-- Adding a table for business details to cover placeholders like business_name, street_address, city, region, postal_code, country, telephone_number, and url
CREATE TABLE business_details (
    business_id UInt32,
    name String,
    street_address String,
    city String,
    region String,
    postal_code String,
    country String,
    telephone_number String,
    url String,
    latitude Float64,
    longitude Float64,
    PRIMARY KEY (business_id)
) ENGINE = MergeTree ORDER BY business_id;

-- The main table for car rentals combining all aspects
CREATE TABLE car_rentals (
    rental_id UInt32,
    city_id UInt32,
    suburb_id UInt32,
    car_brand_id UInt32,
    car_model_id UInt32,
    price_range_id UInt32,
    season_id UInt32,
    offer_id UInt32,
    car_type_id UInt32,
    feature_id UInt32,
    mileage_range_id UInt32,
    PRIMARY KEY (rental_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    FOREIGN KEY (suburb_id) REFERENCES suburbs(suburb_id),
    FOREIGN KEY (car_brand_id) REFERENCES car_brands(brand_id),
    FOREIGN KEY (car_model_id) REFERENCES car_models(model_id),
    FOREIGN KEY (price_range_id) REFERENCES price_ranges(price_range_id),
    FOREIGN KEY (season_id) REFERENCES holiday_seasons(season_id),
    FOREIGN KEY (offer_id) REFERENCES special_offers(offer_id),
    FOREIGN KEY (car_type_id) REFERENCES car_types(car_type_id),
    FOREIGN KEY (feature_id) REFERENCES car_features(feature_id),
    FOREIGN KEY (mileage_range_id) REFERENCES mileage_ranges(mileage_range_id)
) ENGINE = MergeTree ORDER BY rental_id;