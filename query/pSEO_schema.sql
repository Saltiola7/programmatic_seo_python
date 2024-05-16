CREATE TABLE 24rent.my_table
(
    city String,
    main_content String,
    url String,
    page_title String
)
ENGINE = MergeTree
ORDER BY city;