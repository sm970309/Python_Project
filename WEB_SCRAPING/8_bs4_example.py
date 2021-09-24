import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=641253&weekday=fri"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")   # soup 객체로 만들기
cartoons = soup.find_all("td",attrs={"class":"title"})
ratings = soup.find_all("div",attrs={"class":"rating_type"})

total_rate = 0

for cartoon,rating in zip(cartoons,ratings):
    print(cartoon.a.get_text())
    rate = rating.strong.get_text()
    total_rate += float(rate)
    print("평점: "+ rate)
    print("https://comic.naver.com"+cartoon.a['href'])

print("전체 평점: ",total_rate/len(ratings))