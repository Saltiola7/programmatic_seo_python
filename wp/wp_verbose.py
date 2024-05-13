from wordpress_xmlrpc import Client, WordPressPage  # Import necessary libraries for WordPress interaction
from wordpress_xmlrpc.methods.posts import NewPost  # Use NewPost for creating new posts or pages

def read_csv(file_path):
    """
    Reads a CSV file containing city names and returns a list of those cities.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of city names.
    """

    city_list = []
    with open(file_path, 'r') as file:
        # Assuming the CSV has a header named "city", skip the first line
        next(file)  
        for line in file:
            city_name = line.strip()  # Remove leading/trailing whitespace
            city_list.append(city_name)
    return city_list

def replace_city_in_article(article_content, city_name):
    """
    Replaces all occurrences of "Dunedin" in the article content with the given city name.

    Args:
        article_content (str): The content of the article.
        city_name (str): The name of the city to replace "Dunedin" with.

    Returns:
        str: The modified article content with the city name replaced.
    """

    return article_content.replace("Dunedin", city_name)

def publish_to_wordpress(title, content):
    """
    Publishes a new page to a WordPress site with the given title and content.

    Args:
        title (str): The title of the WordPress page.
        content (str): The content of the WordPress page.
    """

    ### Put your website login here (replace placeholders with your actual credentials)
    site_url = 'http://your-wordpress-site.com/xmlrpc.php'
    username = 'your_username'
    password = 'your_password'

    client = Client(site_url, username, password)  # Establish connection to WordPress site
    page = WordPressPage()  # Create a WordPressPage object to represent the new page

    page.title = title  # Set the title of the page
    page.content = content  # Set the content of the page
    page.post_status = 'publish'  # Set the status to 'publish' to make it immediately visible

    page_id = client.call(NewPost(page))  # Use NewPost method to create the page on the WordPress site
    print(f"Page published with ID: {page_id}")  # Print confirmation message with the ID of the published page

def main():
    """
    Main function that orchestrates the entire process:
    1. Reads the input article content from a text file.
    2. Reads a list of cities from a CSV file.
    3. For each city, replaces "Dunedin" in the article and publishes it as a new WordPress page.
    """

    # Read the input article content from input.txt (replace with your actual path)
    input_article_path = 'path/to/input.txt' 
    with open(input_article_path, 'r') as input_file:
        article_content = input_file.read()

    # Read the list of cities from data.csv (replace with your actual path)
    csv_file_path = 'path/to/data.csv' 
    city_list = read_csv(csv_file_path)

    # Iterate through each city in the list
    for city_name in city_list:
        modified_content = replace_city_in_article(article_content, city_name)  # Replace "Dunedin" with the current city

        # Set a title for the WordPress post using the city name
        post_title = f"Best SEO Services In {city_name} FL"  

        # Publish the modified content as a new page on WordPress
        publish_to_wordpress(post_title, modified_content)

if __name__ == "__main__":
    main()  # Run the main function when the script is executed