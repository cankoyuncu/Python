import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

html = requests.get(url).content

print(html)