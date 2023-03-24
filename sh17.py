import requests
from bs4 import BeautifulSoup

req = requests.get("https://books.toscrape.com/")
source = req.content
soup = BeautifulSoup(source,"lxml")
articles = soup.find_all("article",class_="product_pod")
for article in articles:
    h3_tag= article.find("h3")
    a_tag= h3_tag.find("a")
    name = a_tag["title"]
    div = article.find("div", class_="product_price")
    p_tag = div.find("p")
    price = p_tag.text
    name = h3_tag.text
    
    print(name,price)
