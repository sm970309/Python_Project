import requests
"""
res = requests.get("http://naver.com")
print("응답코드 :", res.status_code)    # 200: 정상

if res.status_code==requests.codes.ok:
    print("정상입니다")
else:
    print("에러 코드: ",res.status_code)

res.raise_for_status()
print("웹 스크래핑을 진행합니다")
"""

# 윗 부분을 다음과 같이 두줄로 진행
res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)