import requests
import re

def query_clickhouse(sql, url, headers, auth, method='POST'):
    response = requests.request(method, url, data=sql, headers=headers, auth=auth)
    if response.text:
        return response.text.splitlines()
    else:
        return []

def fetch_data(query, table):
    clickhouse_config = {
        "url": "https://zzd2xg9oti.europe-west4.gcp.clickhouse.cloud:8443",
        "username": "default",
        "password": "~H3YDQCVnwaa4",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }
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
    clickhouse_config = {
        "url": "https://zzd2xg9oti.europe-west4.gcp.clickhouse.cloud:8443",
        "username": "default",
        "password": "~H3YDQCVnwaa4",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }
    auth = (clickhouse_config['username'], clickhouse_config['password'])
    # Batch insert
    values_str = ', '.join(f"('{s}')" for s in sentences)
    query_clickhouse(f"INSERT INTO lvi_programmatic_keywords (programmatic_keywords) VALUES {values_str}", clickhouse_config['url'], clickhouse_config['headers'], auth, method='POST')

def main():
    programmatic_structures_query = "SELECT programmatic_structure FROM default.lvi_programmatic_structures"
    cities_query = "SELECT city FROM default.fi_cities"
    programmatic_structures = fetch_data(programmatic_structures_query, 'lvi_programmatic_structures')
    cities = fetch_data(cities_query, 'fi_cities')

    all_sentences = []
    for structure in programmatic_structures:
        sentences = generate_combinations(structure, cities)
        all_sentences.extend(sentences)

    insert_into_clickhouse(all_sentences)

if __name__ == "__main__":
    main()