html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Basic Html </title>
</head>
<body>
<div class="group1">
<h1 id="header">Python</h1>
<h3>H3 Title</h3>
</div>

<div class="group2">
<ul>
<li>Menu1</li>
<li>Menu2</li>
<li>Menu3</li>
</ul>
</div>

<img src="image_url.jpg" alt="">

<a href="https://www.w3schools.com/">Visit W3Schools.com!</a>
<a href="https://www.w4schools.com/">Visit W3Schools.com!</a>
<a href="https://www.w5schools.com/">Visit W3Schools.com!</a>

</body>
</html>
"""

#Detail: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1.string
result = soup.h3.string
result = soup.h1.name

result = soup.find_all('h1')
result = soup.find_all('h1')[0]

result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul
result = soup.find_all('div')[1].ul.li
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()

result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

# result = soup.find_all('a')
# for link in result:
#     print(link)

result = soup.find_all('a')
for link in result:
    print(link.get('href'))

# print(result)