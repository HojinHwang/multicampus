# 문자열 함수
# 문자열변수.count(찾는 문자) - 갯수 변환

myStr = 'Python string Victory'
print(myStr)
print('myStr 문자열은 {}'.format(myStr))
print('myStr 문자열은 %s'% (myStr))
print(myStr.count('y'))  # y가 몇개있는지 세어줌
num = myStr.count('y')
print(type(num)) # 정수 int

# 문자열변수.find(찾는 문자) - 위치반환
# - 위치 반환
# 반환값이 -1 이라면 찾는 문자가 없다.
print('첫번째 글자는 ? {} '.format(myStr[0]))
print('3-5 글자 반환 ? {}'.format(myStr[2:5])) # 마지막 인덱스는 뽑지 않는다. -1
print(myStr.find('s')) #7 , 공백도 친다
print(type(myStr.find('s'))) # 정수 int
print(myStr.find('P'))
print(myStr.find('k'))
a= ","
a.join('abcd')

# 구분자변수 .join(문자열이나 문자열 변수)
sep = ' / '
print(sep.join('12345'))

# 문자열을 대소문자로 변경
# 문자열변수 .upper()
# 문자열변수 .lower()
print(myStr.upper()) # 대문자
print(myStr.lower()) # 소문자
print(myStr) # 원본

# 문자열변수.strip()
# 문자열안에 공백 삭제
myStr = '  Python string Victory  '
print(myStr.strip()) # 공백 삭제
print(myStr) # 원본
result = myStr.strip()
print(result)

# 문자열변수.replace('찾는문자', '교체문자')
a = 'Life is too short'
a.replace('Life', 'Your leg')
print(a)
print(a.replace('Life','Your leg'))

# 퀴즈
# 다음과 같이 교체한다.
'''
좋아하는 꽃 - 장미
좋아하는 꽃 - 백합
좋아하는 flower - 백합
'''

favorite = '좋아하는 꽃 - 장미'
print(favorite.replace('장미','백합'))
favorite1 = favorite.replace('장미','백합')
print(favorite1.replace('꽃','flower'))
# 퀴즈
# 다음과 같은 결과값이 출력되도록 한다.
'''
Let thy speech be short, comprehending much in few words.
첫번째 t의 위치 : 3
첫번째 m의 위치 : 28
s 의 갯수 : 3
= 으로 연결 :
L=e=t =t=h=y= =s=p=e=e=c=h= =b=e= =s=h=o=r=t=,= =c=o=m=p=r=e=h=e=n=d=i=n=g= =m=u=c=h= =i=n= =f=e=w= =w=o=r=d=s=
대문자로 변경 :
LET THE SPEECH BE SHORT, COMPREHENDING MUCH IN FEW WORDS.
'''

a = 'Let thy speech be short, comprehending much in few words.'
print(a.find('t'))
print(a.find('m'))
print(a.count('s'))
print(a.upper())
b ='='
print(b.join(a))