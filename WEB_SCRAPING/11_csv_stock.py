import requests
from bs4 import BeautifulSoup
import csv
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일 저장하는 방법
filename = "시가총액1-200.csv"
f = open(filename,'w',encoding="utf-8-sig",newline="")
writer = csv.writer(f)

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # 제목 집어넣기
    if page==1:
        titles = soup.find("table",attrs={"class":"type_2"}).find("thead").find_all("th")
        title = [t.get_text() for t in titles]
        writer.writerow(title[:-1])

    # 내용 집어넣기
    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        cols = row.find_all("td")
        if len(cols)<=1:
            continue
        data = [col.get_text().strip() for col in cols]
        writer.writerow(data)