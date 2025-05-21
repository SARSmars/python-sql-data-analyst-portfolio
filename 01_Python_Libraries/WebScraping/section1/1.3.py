# Python Web Scraping Tutorial. Use BeautifulSoup & Requests to scrape & crawl Craigslist directory with Python
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Oxford"
import requests
response = requests.get(url)
response
# Check if the request was successful
print(response.status_code)