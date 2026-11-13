# open the URL https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data using  urllib.request.urlopen(url) and print out the response you get. What is this and how do you work with it? You will need to import urllib.request and ssl. Set ssl._create_default_https_context = ssl._create_unverified_context

import ssl
import urllib.request   

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

response = urllib.request.urlopen(url)
print(response) 
# Use the opened URL to get the HTML as lines. Decode each line .decode('utf-8') and print out the line only if it has a <title> tag.

for line in response.readlines():
# print(line)
    decoded_line = line.decode('utf-8')
    if '<title>' in decoded_line:
        print(decoded_line)