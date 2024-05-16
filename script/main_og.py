import re
from itertools import product
import yaml

def load_config(config_file):
    """Loads configuration from a YAML file."""
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def parse_placeholders(structure):
    """Extracts placeholders from a programmatic structure."""
    return re.findall(r'\{(.*?)\}', structure)

def fetch_placeholder_values(placeholder, data_tables, current_brand=None):
    """Fetches values for a placeholder from the data tables, adjusted for nested car models and other placeholders."""
    if placeholder == 'car_model' and current_brand:
        return data_tables['car_brand'].get(current_brand, [])
    elif placeholder in data_tables:
        return data_tables[placeholder]
    else:
        print(f"Warning: Data not found for placeholder '{placeholder}'. Skipping...")
        return []

def generate_combinations(programmatic_structure, data_tables):
    """Generates combinations for a given structure using data tables."""
    placeholders = parse_placeholders(programmatic_structure)
    all_combinations = []
    for brand in data_tables['car_brand'].keys():
        # Prepare values for each placeholder based on available data
        placeholder_values = {ph: [] for ph in placeholders}  # Initialize dictionary for all placeholders
        placeholder_values['car_brand'] = [brand]  # Set brand
        placeholder_values['car_model'] = fetch_placeholder_values('car_model', data_tables, current_brand=brand)

        # For other placeholders like 'city', 'holiday', etc., populate from data_tables if available
        for ph in placeholders:
            if ph not in ['car_brand', 'car_model']:  # These are already handled
                placeholder_values[ph] = fetch_placeholder_values(ph, data_tables)

        # Now generate combinations
        combinations = product(*(placeholder_values[ph] for ph in placeholders if placeholder_values[ph]))  # Ensure non-empty lists
        for combination in combinations:
            result = programmatic_structure
            for placeholder, value in zip(placeholders, combination):
                result = result.replace(f"{{{placeholder}}}", str(value))
            all_combinations.append(result)
    return all_combinations

def main():
    """Main function to generate and print combinations."""
    config_file = 'config.yml'
    config = load_config(config_file)
    for structure in config['programmatic_structures']:
        print(f"Combinations for Structure: '{structure}'")
        combinations = generate_combinations(structure, config['data_tables'])
        for combination in combinations:
            print(combination)

if __name__ == "__main__":
    main()