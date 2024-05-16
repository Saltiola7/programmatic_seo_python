INSERT INTO schema_org_templates (template_id, template_name, markup_template, description) 
VALUES
(
    2, 
    'LocalBusiness', 
    '{
        "@context": "http://schema.org",
        "@type": "LocalBusiness",
        "name": "{business_name}",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "{street_address}",
            "addressLocality": "{city}",
            "addressRegion": "{region}",
            "postalCode": "{postal_code}",
            "addressCountry": "{country}"
        },
        "telephone": "{telephone_number}",
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "{latitude}",
            "longitude": "{longitude}"
        },
        "url": "{url}"
    }', 
    'Template for local business pages'
),
(
    3, 
    'Offer', 
    '{
        "@context": "http://schema.org",
        "@type": "Offer",
        "itemOffered": {
            "@type": "Product",
            "name": "{product_name}",
            "description": "{product_description}",
            "image": "{product_image_url}"
        },
        "price": "{price}",
        "priceCurrency": "{currency}",
        "availability": "http://schema.org/{availability}",
        "validFrom": "{valid_from_date}"
    }', 
    'Template for offer pages'
),
(
    4, 
    'Review', 
    '{
        "@context": "http://schema.org",
        "@type": "Review",
        "itemReviewed": {
            "@type": "Thing",
            "name": "{item_name}"
        },
        "author": {
            "@type": "Person",
            "name": "{author_name}"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "{rating_value}",
            "bestRating": "{best_rating}",
            "worstRating": "{worst_rating}"
        },
        "reviewBody": "{review_body}"
    }', 
    'Template for review pages'
);