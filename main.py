import requests
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('cfg/.env')

def get_clickhouse_config():
    return {
        "url": os.getenv("CLICKHOUSE_URL"),
        "username": os.getenv("CLICKHOUSE_USERNAME"),
        "password": os.getenv("CLICKHOUSE_PASSWORD"),
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }

def query_clickhouse(sql, url, headers, auth, method='POST'):
    response = requests.request(method, url, data=sql, headers=headers, auth=auth)
    if response.text:
        return response.text.splitlines()
    else:
        return []

def fetch_data(query):
    clickhouse_config = get_clickhouse_config()
    auth = (clickhouse_config['username'], clickhouse_config['password'])
    return query_clickhouse(query, clickhouse_config['url'], clickhouse_config['headers'], auth)

def parse_placeholders(structure):
    return re.findall(r'\{(.*?)\}', structure)

def generate_combinations(programmatic_structure, cities):
    placeholders = parse_placeholders(programmatic_structure)
    all_combinations = []
    for city in cities:
        result = programmatic_structure
        for placeholder in placeholders:
            result = result.replace(f"{{{placeholder}}}", city)
        all_combinations.append(result)
    return all_combinations

def insert_into_clickhouse(sentences):
    clickhouse_config = get_clickhouse_config()
    auth = (clickhouse_config['username'], clickhouse_config['password'])
    # Batch insert
    values_str = ', '.join(f"('{s}')" for s in sentences)
    query_clickhouse(f"INSERT INTO lvi_programmatic_keywords (programmatic_keywords) VALUES {values_str}", clickhouse_config['url'], clickhouse_config['headers'], auth, method='POST')

def main():
    programmatic_structures_query = "SELECT programmatic_structure FROM default.lvi_programmatic_structures"
    cities_query = "SELECT city FROM default.fi_cities"
    programmatic_structures = fetch_data(programmatic_structures_query)
    cities = fetch_data(cities_query)

    all_sentences = []
    for structure in programmatic_structures:
        sentences = generate_combinations(structure, cities)
        all_sentences.extend(sentences)

    insert_into_clickhouse(all_sentences)

if __name__ == "__main__":
    main()