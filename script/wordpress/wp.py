from wordpress_xmlrpc import Client, WordPressPage  # Import WordPressPage
from wordpress_xmlrpc.methods.posts import NewPost  # Use NewPost for both posts and pages

def read_csv(file_path):
    city_list = []
    with open(file_path, 'r') as file:
        # Assuming the CSV has a header named "city"
        next(file)  # Skip the header
        for line in file:
            city_name = line.strip()
            city_list.append(city_name)
    return city_list

def replace_city_in_article(article_content, city_name):
    # Replace occurrences of "Dunedin" with the current city name
    return article_content.replace("Dunedin", city_name)

def publish_to_wordpress(title, content):
    ### Put your website login here
    site_url = 'http://your-wordpress-site.com/xmlrpc.php'
    username = 'your_username'
    password = 'your_password'

    client = Client(site_url, username, password)

    page = WordPressPage()  # Create a WordPressPage object
    page.title = title
    page.content = content
    page.post_status = 'publish'

    page_id = client.call(NewPost(page))  # Use NewPost with a WordPressPage object to publish a page
    print(f"Page published with ID: {page_id}")

def main():
    # Read the input article content from input.txt
    input_article_path = 'path/to/input.txt' # Change The Path
    with open(input_article_path, 'r') as input_file:
        article_content = input_file.read()

    # Read the list of cities from data.csv
    csv_file_path = 'path/to/data.csv' # Change The Path
    city_list = read_csv(csv_file_path)

    # Iterate through each city, replace in the article, and publish
    for city_name in city_list:
        modified_content = replace_city_in_article(article_content, city_name)

        # Set a title for the WordPress post
        post_title = f"Best SEO Services In {city_name} FL"

        # Publish the post to WordPress
        publish_to_wordpress(post_title, modified_content)

if __name__ == "__main__":
    main()
