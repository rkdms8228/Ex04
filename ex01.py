import requests
from bs4 import BeautifulSoup

###################################################
#랭킹추출
###################################################

#1.사이트에 요청 응답(html)을 받기  - requests
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

#요청하기
response = requests.get(url);

#응답확인
print(response.status_code)  #상태코드
html = response.text         #html코드
#print(html)


#2.필요한 태그 추출하기 - BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")

tags = soup.select(".tit3>a")   #* 전략을 잘 세워야 함
#print(tags[0].text)

'''
for tag in tags:
    title = tag.text
    print(title)
'''

for index, tag in enumerate(tags):     #index값도 같이 사용할때 enumerate() 사용
    rank = index + 1
    title = tag.text
    print(rank, title)