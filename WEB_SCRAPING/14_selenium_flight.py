from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

# 가는 날 선택
elems = browser.find_elements_by_tag_name("button")
elems[10].click()


