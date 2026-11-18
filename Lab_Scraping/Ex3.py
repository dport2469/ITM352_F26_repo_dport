import pandas as pd
import ssl
from bs4 import BeautifulSoup
import requests

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"

# Using BeautifulSoup, parse the page to extract the HTML. What object do you get and how is this useful? Use prettify() to print out the HTML (only put the first few lines here). 


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()[:500])  # Print only the first 500 characters of the prettified HTML

people_cards = soup.find_all('article', class_='node node-faculty node-type-itm-faculty view-mode-teaser')

print(f"Found {len(people_cards)} people cards.")
print(f"First article:\n{people_cards[0].prettify()}") 

for article in people_cards:
    name = article.find('h2', class_='title').get_text(strip=True)
    email = article.select_one('.field-email .field-item').get_text(strip=True)
    print(f"Name: {name}, Email: {email}")
