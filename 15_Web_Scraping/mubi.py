import requests
from bs4 import BeautifulSoup

url = "https://mubi.com/tr/lists/the-best-films-of-every-year"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

film_list = soup.find_all(class_="css-liprzy eode0fa0")

for film in film_list:
    title = film.find_all(class_="css-f1nzx1 e1m2oid7")
    if title:
        title = title[0].text
    else:
        title = "No title found"

    date = film.find_all(class_="css-f0gmrr e1m2oid8")
    if date:
        date = date[0].text
    else:
        date = "No date found"

    print(f"Title: {title}, Date: {date}")
