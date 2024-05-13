import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def count_pages_from_sitemap(sitemap_url):
    pages = []
    sub_sitemaps = []

    # Fetch the initial sitemap
    sitemap_xml = requests.get(sitemap_url).content
    soup = BeautifulSoup(sitemap_xml, 'xml')

    # Find all the page URLs in the initial sitemap
    for url in soup.find_all('loc'):
        page_url = url.text
        if page_url.endswith('.xml'):
            sub_sitemaps.append(page_url)
        else:
            pages.append(page_url)

    # Recursively fetch sub-sitemaps and add their pages
    for sub_sitemap_url in sub_sitemaps:
        pages.extend(count_pages_from_sitemap(sub_sitemap_url))

    return pages

# Example usage
website_sitemap = 'https://24rent.fi/sitemap.xml'
all_pages = count_pages_from_sitemap(website_sitemap)
print(f'Total number of pages: {len(all_pages)}')

