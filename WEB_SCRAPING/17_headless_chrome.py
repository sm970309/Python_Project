from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 크롬을 백그라운드로 실행
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# user-agent 설정을 안해주면 headless chrome으로 뜨게 됨
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

browser = webdriver.Chrome(options=options)
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

browser.get_screenshot_as_file("google_movie.png")

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
