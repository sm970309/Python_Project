from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

time.sleep(3)

# 출발지 선택(서울)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(1)
browser.find_element_by_xpath('//button[text()="국내"]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[1]').click()

# 도착지 선택(제주)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//button[text()="국내"]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]').click()

# 가는 날 선택
browser.find_element_by_xpath('//button[text()="가는 날"]').click()
time.sleep(2)
browser.find_elements_by_xpath('//b[text()="27"]')[0].click()
browser.find_elements_by_xpath('//b[text()="28"]')[0].click()

time.sleep(1)
# 항공권 검색
browser.find_element_by_xpath('//span[text()="항공권 검색"]').click()

# 조건에 따라서 기다리기(XPATH 기준 -> 해당 element가 나올때 까지)
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_elements_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]')))
    new_list = elem.text.split('\n')
    print(new_list)

finally:
    browser.quit()