# 필요한 모듈 불러오기  
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = """
<html>
    <body>
    <h1 id='title'>Hello Python</h1>
    <p id='body'>웹페이지 분석</p>
    <p>웹스크래핑</p>
    <ul>
        <li class='fruit'>사과</li>
        <li>양파</li>
        <li>고구마</li>
        <li class='fruit'>바나나</li>
    </ul>
    <ul id='linkBox'>
        <li><a href='http://naver.com'>Naver</a></li>
        <li class='nateClass'><a href='http://nate.com'>Nate</a></li>
        <li><a href='http://google.com'>Google</a></li>
        <li><a href='http://yahoo.com'>Yahoo</a></li>
        <li><a href='http://daum.com'>Daum</a></li>
    </ul>
    <div>
       <img src="images/naver.png" alt="naver">
       <img src="images/google.png" alt="google">
       <img src="images/coupang.png" alt="coupang">
       <img src="images/daum.png" alt="daum">
    </div>
    </body>
</html>
"""
# 뷰디풀숲 객체 생성 
bs= BeautifulSoup(html,"html.parser")

# CSS 셀렉터로 찾아가기 - 1개만 추출
# bs.select_one('CSS 셀렉터')
# 문서에서 ul 태그 아래있는 첫번째 li 추출
print(bs.select_one('ul li'))
# 문서에서 div 태그 아래있는 첫번째 img 추출
print(bs.select_one('div img'))
# 문서에서 linkBox 아이디값을 가진 태그안에 있는
# li 태그에서 다시 아래있는 첫번째 a 추출
print(bs.select_one('#linkBox li a'))
# linkBox 아이디값을 가진 ul 태그안에 있는
# nateClass 클래스값을 가진 li 태그안에 있는
# a 태그 
print(bs.select_one('#linkBox .nateClass a'))
print(bs.select_one('ul#linkBox li.nateClass a'))

# 웹상에 있는 페이지 이용
# 웹상의 페이지를 변수로 저장 
html1 = urlopen('http://pythonscraping.com/pages/warandpeace.html') 
print(html1.read())
# 뷰티풀숲 변수로 웹상의 태그 소스와 연결 
bs= BeautifulSoup(html1.read(),"html.parser")
print(bs)
print('\n'*10)

# 웹페이지에서 [Copy selector]기능으로 선택자 복사 
#   #text > span
print('#text > span 소스 확인하기')
print(bs.select_one('span'))