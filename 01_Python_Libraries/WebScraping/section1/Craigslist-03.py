#!/usr/bin/env python
# coding: utf-8
# # GoTrained - Web Scraping with Python - Getting Started
#  
# - Python web scraping libraries you need for the course and how to install them.
# - How to extract URLs from one webpage.
# - How to extract other text data pieces from one webpage.
# - How to crawl multiple webpages and extract data from each of them.
# - How to handle navigation links and move to *next* pages.
# - How to save your scraped data into a CSV file.
# - And finally, a quick overview about *other* popular web scraping frameworks.
from bs4 import BeautifulSoup
import requests 

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

divs = soup.find_all("a", {"class": "icon"})

for div in divs:
    print(div)