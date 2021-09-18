# 정규식 사용법
import re

p = re.compile("ca.e")
# . : 하나의 문자를 의미 ex(ca.e) -> caae,cabe...
# ^ : 문자열의 시작 ex (^de) -> de로 시작하는 모든 문자열
# $ : 문자열의 끝 ex(se$) -> se로 끝나는 모든 문자열

def print_match(m):
    # 매치되지 않으면 에러 발생
    if m:
        print("m.group()",m.group())
        print("m.string",m.string)
        print("m.start()",m.start())
        print("m.end()",m.end())
        print("m.span()",m.span())
        print()
    else:
        print("매칭 X")
# 매칭 시킬때는 '처음부터' 확인
m = p.match("careless")
print_match(m)

# 주어진 문자열 중에 일치하는게 있는지 확인
n = p.search("good care")
print_match(n)

# 일치하는 형태를 리스트 형태로 반환
lst = p.findall("good care cafe")
print(lst)