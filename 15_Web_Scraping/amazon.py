import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/s?bbn=13710018031&rh=n%3A12466496031%2Cn%3A17471820031%2Cn%3A13710018031%2Cn%3A26232650031&dc&qid=1689085218&rnid=13710018031&ref=lp_13710018031_nr_n_0"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"octopus-pc-item octopus-pc-item-v3"}, limit=1)

# for li in list:
#     name = li.div.a.h3.text.strip()
#     link = li.div.a.get("href")
#     print(link)
#     oldprice = li.find("div", {"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
#     newprice = li.find("div", {"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")

print(list) 








# import requests
# from bs4 import BeautifulSoup

# url = "https://www.n11.com/saat/kostekli-saat"

# html = requests.get(url).content
# soup = BeautifulSoup(html, "html.parser")

# title = soup.find("title").text

# print(title)



# import requests
# from bs4 import BeautifulSoup

# url = "https://www.n11.com/saat/kostekli-saat"

# html = requests.get(url).content
# soup = BeautifulSoup(html, "html.parser")

# title = soup.find("title").text

# products = soup.find_all("div", class_="prd-list-item")

# for product in products:
#   name = product.find("a", class_="prd-link").text
#   price = product.find("span", class_="prd-price").text
#   description = product.find("p", class_="prd-desc").text

#   print(f"Name: {name}")
#   print(f"Price: {price}")
#   print(f"Description: {description}")



# import requests
# from bs4 import BeautifulSoup

# url = "https://www.n11.com/saat/kostekli-saat"

# html = requests.get(url).content
# soup = BeautifulSoup(html, "html.parser")

# products = soup.find_all("div", class_="prd-list-item")

# product_data = []

# for product in products:
#   name = product.find("a", class_="prd-link").text
#   old_price = product.find("span", class_="prd-old-price").text
#   new_price = product.find("span", class_="prd-price").text

#   product_data.append({
#     "name": name,
#     "old_price": old_price,
#     "new_price": new_price
#   })

# print(product_data)
