INSERT INTO schema_org_templates (template_id, template_name, markup_template, description) 
VALUES
(
    1, 
    'CarRental', 
    '{
        "@context": "http://schema.org",
        "@type": "AutoRental",
        "name": "{car_brand} {car_model} Rental in {city}",
        "url": "{url}",
        "description": "Rent a {car_brand} {car_model} in {city} for {holiday} with a {discount} discount. Enjoy {event} in {city} with our special package.",
        "offers": {
            "@type": "Offer",
            "price": "{price}",
            "priceCurrency": "EUR"
        },
        "location": {
            "@type": "Place",
            "name": "{city} Rental Location",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "{street_address}",
                "addressLocality": "{city}",
                "addressRegion": "{region}",
                "postalCode": "{postal_code}",
                "addressCountry": "FI"
            }
        }
    }', 
    'Template for car rental pages'
);