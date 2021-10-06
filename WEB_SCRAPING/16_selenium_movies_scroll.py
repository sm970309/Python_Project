from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

#JavaScript 문법
# 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # document.body.scrollHeight -> 스크롤 끝까지 내리기

# 현재 문서의 높이 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height

print("스크롤 완료")

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs={"class":"Vpfmgd"})    # 리스트 형태-> , 사용해서 or 조건

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    link = "https://play.google.com"+link

    print(f"제목: {title}")
    print(f"할인 전 금액{original_price}, 할인 후 금액{price}")
    print(f"링크: {link}")
