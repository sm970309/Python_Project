import requests
from bs4 import BeautifulSoup
import os

for year in range(2014,2021):
    os.mkdir(str(year)+"년")
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    movies = soup.find_all("img",attrs={"class":"thumb_img"})
    titles = soup.find_all("div",attrs={"class":"info_tit"})

    for idx,(movie,title) in enumerate(zip(movies,titles)):
        movie_ulr = movie["src"]
        movie_res=requests.get(movie_ulr)
        image = movie_res.content
        name = title.get_text()

        with open("{}년/movie_{}_{}.jpg".format(year,idx+1,name.replace(":",",")),"wb") as f:
            f.write(image)
        print(str(idx+1),name,movie["src"])
        if idx>=29:
            break