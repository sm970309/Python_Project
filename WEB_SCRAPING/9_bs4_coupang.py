import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
ad_items = soup.find_all("li",attrs={"class":re.compile("search-product search-product__ad-badge")})

for item in items:
    name = item.find("div", attrs={"class": "name"}).get_text()
    if item in ad_items:
        print("-"*len(name)*2)
        print("광고 제품: "+name )
        print("-"*len(name)*2)
        continue

    price = item.find("strong",attrs={"class":"price-value"})
    if price:
        price = price.get_text()
    rating = item.find("em",attrs={"class":"rating"})
    if rating:
        rating = rating.get_text()
    rating_count = item.find("span",attrs={"class":"rating-total-count"})
    if rating_count:
        rating_count = rating_count.get_text()
    print(name,price,rating,rating_count)

print("광고 개수:{}".format(len(ad_items)))
