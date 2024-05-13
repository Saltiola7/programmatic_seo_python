SELECT c.name AS city_name, cb.name AS car_brand, cm.name AS car_model, hs.name AS holiday_season
FROM cities c
JOIN suburbs s ON c.city_id = s.city_id
JOIN car_models cm ON cm.brand_id = cb.brand_id
JOIN car_brands cb ON cb.brand_id = cm.brand_id
JOIN holiday_seasons hs ON hs.name = 'Christmas'
WHERE c.name = 'Helsinki' AND cb.name = 'Toyota' AND cm.name = 'Corolla';