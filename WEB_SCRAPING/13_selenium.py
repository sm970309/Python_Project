from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 크롬 웹드라이브 객체 생성

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://naver.com")

# 너무 빠르게 열려서 클릭 안되는 상황을 막기위해 실행
time.sleep(3)

# 로그인 버튼 클릭
browser.find_element_by_class_name("link_login").click()

# id,pw 입력
browser.find_element_by_id("id").send_keys("naverid")
browser.find_element_by_id("pw").send_keys("naverpw")

# 로그인 버튼 클릭
browser.find_element_by_class_name("btn_login").click()

time.sleep(3)

# 현재 써져있는 글씨 지우기
browser.find_element_by_id("id").clear()

browser.find_element_by_id("id").send_keys("sm970309")
browser.find_element_by_id("pw").send_keys("tjdals39272@")

# html 정보 출력
print(browser.page_source)

# close : 현재 탭만 종료 quit : 전체 탭 종료
browser.quit()