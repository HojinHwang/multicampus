from bs4 import BeautifulSoup
from urllib.request import urlopen # 웹사이트로 접근

html = urlopen("http://www.nlotto.co.kr/gameResult.do?method=byWin")

soup = BeautifulSoup(html, "html.parser")
# print(soup)
h3 = soup.find("h3", {"class":"result_title"}) # 객체.메소드(목표)
hoi = h3.strong.string
print(hoi, "회")
number = []
p = soup.find("p", {"class":"number"})
imgs = p.find_all("img")
# print(imgs)
for img in imgs:
    alt = img["alt"]
    number.append(alt)
bonus = number.pop() # pop = 마지막 값 뽑아냄
print(number)
print('보너스 번호 =', bonus)