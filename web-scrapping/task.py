"""
Finish the script. It should retrieve the main pages of websites below (1p) and find 10 unique internal links on each of them (1p).
Then, it should count the number of outbound links (`a` tags marked as outside links by the function below) (1.5p) and images (`img` tags) (1.5p) on every site.
Send me the script.
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_outside_link(current_site, link):
    domain = urlparse(current_site).netloc
    link_domain = urlparse(link).netloc
    return link_domain and link_domain != domain

news_websites = [
    'https://www.cnn.com',
    'https://www.bbc.com',
    'https://www.nytimes.com',
    'https://www.foxnews.com',
    'https://www.theguardian.com',
    'https://www.nbcnews.com',
    'https://www.wsj.com',
    'https://www.usatoday.com',
    'https://www.reuters.com',
    'https://www.bloomberg.com',
    'https://www.apnews.com',
]
