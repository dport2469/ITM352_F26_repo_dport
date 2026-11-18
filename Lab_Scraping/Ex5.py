import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

response = requests.get(url)
response.raise_for_status()
records = response.json()
print(records)