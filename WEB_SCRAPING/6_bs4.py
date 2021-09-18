import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")   # soup 객체로 만들기

print(soup.title.get_text())
print(soup.a)   # 첫번째로 발견되는 a태그 출력
print(soup.a.attrs) # attrs -> 속성 확인
print(soup.a["href"])   #[] 안의 속성만 출력


rank1 = soup.find("li",attrs={"class": "rank01"})
print(rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling -> 이 부분을 밑에처럼 쓸 수 있음
rank2= rank1.find_next_sibling("li")    # li 태그를 가진 다음 sibling을 찾음
print(rank2.a.get_text())

rank3 = rank2.next_sibling.next_sibling
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
# 부모로 이동 가능
print(rank1.parent.a.get_text())
# siblings 도 가능
print(rank1.find_next_siblings("li"))

print(soup.find("a", title = "프리드로우-제405화 파이트 클럽 (7)"))