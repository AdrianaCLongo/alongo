import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
    }

page = requests.get("https://www.tn.gov/tdot/projects.html, headers=headers")
url ='https://www.tn.gov/tdot/projects.html'

# get response and soup object
response = requests.get(url, headers=headers)
soup = bs (page.content, 'html.parser')
soup = bs(response.text, 'lxml')

# find all 'a' tags with urls
proj_urls = soup.select_one('div.template-left-nav.tn-leftnav > div').text

print(proj_urls)

time.sleep(2)