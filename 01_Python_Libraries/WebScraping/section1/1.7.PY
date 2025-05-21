# Creawling and Scraping Next Page
# USE THE TAGE TO GET HTE BUTTON TO THE NEXT PAGE


from bs4 import BeautifulSoup
import requests 


url = "https://sipp.iitk.ac.in/sign-in"
response =  requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')
print(soup)
