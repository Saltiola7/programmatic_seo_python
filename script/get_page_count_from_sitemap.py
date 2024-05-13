import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def query_clickhouse(sql, url, headers, auth, method='POST'):
    response = requests.request(method, url, data=sql, headers=headers, auth=auth)
    if response.text:
        return response.text.splitlines()
    else:
        return []

def fetch_data(query):
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

def count_pages_from_sitemap(sitemap_url):
    pages = []
    sub_sitemaps = []

    sitemap_xml = requests.get(sitemap_url).content
    soup = BeautifulSoup(sitemap_xml, 'xml')

    for url in soup.find_all('loc'):
        page_url = url.text
        if page_url.endswith('.xml'):
            sub_sitemaps.append(page_url)
        else:
            pages.append(page_url)

    for sub_sitemap_url in sub_sitemaps:
        pages.extend(count_pages_from_sitemap(sub_sitemap_url))

    return pages

def get_sitemap_url(url):
    try:
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}/sitemap.xml"
    except ValueError as e:
        print(f"Error parsing URL: {url}")
        print(f"Error message: {str(e)}")
        return None

def analyze_sitemap(sitemap_url):
    try:
        pages = count_pages_from_sitemap(sitemap_url)
        return len(pages)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {sitemap_url}")
        print(f"Error message: {str(e)}")
        return None

def main():
    query = "SELECT url FROM `24Rent`.`24Rent_google_autonvuokraus_autonvuokraus_tampere`"
    urls = fetch_data(query)
    results = []
    processed_sitemaps = set()

    for url in urls:
        sitemap_url = get_sitemap_url(url)
        if sitemap_url is None or sitemap_url in processed_sitemaps:
            continue
        print(f"Processing sitemap: {sitemap_url}")
        pages_count = analyze_sitemap(sitemap_url)
        results.append({"sitemap_url": sitemap_url, "pages": pages_count})
        processed_sitemaps.add(sitemap_url)

    df = pd.DataFrame(results)
    df.to_csv("sitemap_results.csv", index=False)
    return df

if __name__ == "__main__":
    df = main()
    print(df)