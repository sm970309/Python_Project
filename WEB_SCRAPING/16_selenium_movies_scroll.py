from selenium import webdriver
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
