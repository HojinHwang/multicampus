from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://nlotto.co.kr/gameResult.do?method=byWin")
soup = BeautifulSoup(html, "html.parser")
h3 = soup.find("h3", {"class":"result_title"})
hoi = h3.strong.string
print(hoi, "회")
number = []
p = soup.find("p", {"class":"number"})
imgs = p.find_all("img")
# print(imgs)
for img in imgs:
    alt = img["alt"]
    number.append(alt)
bonus = number.pop() # pop 은 마지막 값(보너스) 뽑기
print(number)
print("보너스 번호=", bonus)
