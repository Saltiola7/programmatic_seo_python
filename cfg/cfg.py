import requests
from requests.auth import HTTPBasicAuth
import yaml
import os
import clickhouse_connect

def load_configuration():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, 'cfg.yml')

    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)['clickhouse']
    except Exception as e:
        print(f"Error loading configuration: {str(e)}")
        exit(1)

def execute_query():
    config = load_configuration()
    response = requests.post(
        config['url'],
        data=config['query'],
        auth=HTTPBasicAuth(config['username'], config['password']),
        headers=config['headers']
    )

    if response.status_code == 200:
        print("Query executed successfully!")
        print("Response:", response.text)
    else:
        print("Failed to execute query.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)



def connect_to_clickhouse():
    # Load configuration from cfg.yml
    with open('cfg/cfg.yml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Extract ClickHouse connection details
    ch_config = config['clickhouse']
    host = ch_config['url'].split("//")[1].split(":")[0]
    user = ch_config['username']
    password = ch_config['password']
    query = ch_config['query']

    # Create a ClickHouse client
    client = clickhouse_connect.get_client(
        host=host,
        user=user,
        password=password,
        secure=True
    )

    # Execute the query and return the result
    result = client.query(query).result_set[0][0]
    return result