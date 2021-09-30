from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 크롬 웹드라이브 객체 생성
browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://naver.com")

# 해당 클래스를 찾아서 변수화
elem = browser.find_element_by_class_name("link_login")
# 클릭
elem.click()

# 글자 보내기
elem = browser.find_element_by_id("query")
elem.send_keys("주식")
# 해당 키를 누르는 효과
elem.send_keys(Keys.ENTER)

# 태그로 검색(여러개)
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")

# 검색 버튼 누르기
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()