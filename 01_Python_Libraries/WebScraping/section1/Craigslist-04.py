from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

# Update this selector based on the new structure
jobs = soup.find_all('li', {'class': 'checkbox'})

for job in jobs:
    # Update the selectors below as needed
    print(job)