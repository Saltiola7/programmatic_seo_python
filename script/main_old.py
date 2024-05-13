import sqlite3
import re
from itertools import product

def connect_to_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        exit(1)

def load_programmatic_structures_from_db(cursor):
    try:
        cursor.execute("SELECT structure FROM programmatic_structure")
        return [item[0] for item in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"An error occurred while loading programmatic structures: {e}")
        return []

def fetch_data(cursor, query):
    try:
        cursor.execute(query)
        return [item[0] for item in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def parse_placeholders(programmatic_structures):
    placeholder_pattern = re.compile(r'\{(.*?)\}')
    placeholders = set()
    for structure in programmatic_structures:
        found_placeholders = placeholder_pattern.findall(structure)
        placeholders.update(found_placeholders)
    return placeholders

def fetch_placeholder_queries(cursor, placeholders):
    placeholder_queries = {}
    for placeholder in placeholders:
        column_name = 'name' if placeholder not in ['price_range', 'mileage', 'feature', 'amenity', 'seating_capacity', 'location_description'] else 'description'
        table_name = placeholder
        query = f"SELECT DISTINCT {column_name} FROM {table_name}"
        placeholder_queries[placeholder] = fetch_data(cursor, query)
    return placeholder_queries

def generate_combinations(programmatic_structures, placeholder_queries):
    all_combinations = []
    for structure in programmatic_structures:
        relevant_placeholders = {placeholder: placeholder_queries[placeholder] for placeholder in placeholder_queries if placeholder in structure}
        for combination in product(*relevant_placeholders.values()):
            result = structure
            for placeholder, value in zip(relevant_placeholders.keys(), combination):
                result = result.replace(f"{{{placeholder}}}", value)
            all_combinations.append(result)
    return all_combinations

def write_combinations_to_file(output_path, all_combinations):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for combination in all_combinations:
                file.write(combination + '\n')
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    db_path = '/Users/tis/foam/github/24Rent_SEO/data/data.sqlite'
    output_path = '/Users/tis/foam/github/24Rent_SEO/output_combinations.txt'

    conn = connect_to_database(db_path)
    cursor = conn.cursor()

    programmatic_structures = load_programmatic_structures_from_db(cursor)
    placeholders = parse_placeholders(programmatic_structures)
    placeholder_queries = fetch_placeholder_queries(cursor, placeholders)
    all_combinations = generate_combinations(programmatic_structures, placeholder_queries)
    write_combinations_to_file(output_path, all_combinations)

    conn.close()
    print("All combinations have been generated and saved to output_combinations.txt.")

if __name__ == "__main__":
    main()