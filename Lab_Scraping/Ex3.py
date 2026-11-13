import pandas as pd
import ssl
from bs4 import BeautifulSoup
import requests

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"

# Using BeautifulSoup, parse the page to extract the HTML. What object do you get and how is this useful? Use prettify() to print out the HTML (only put the first few lines here). 


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:50])  # Print only the first 500 characters of the prettified HTML
