# 퀴즈
# 다음과 같이 교체한다.
'''
좋아하는 꽃 - 장미
좋아하는 꽃 - 백합
좋아하는 flower - 백합
'''

a = '좋아하는 꽃 - 장미'
print(a.replace('장미','백합'))
b = a.replace('장미','백합')
print(b.replace('꽃','flower'))

# 퀴즈
# 공백 없이 프린트하여라
myStr = '  Python string Victory  '
print(myStr.strip())
print(myStr)

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

myString = 'Let thy speech be short, comprehending much in few words.'
print(myString.find('t'))
print(myString.find('m'))
print(myString.count('s'))
c ='='
print(c.join(myString))
print(myString.upper())

# 퀴즈
'''
2개의 리스트를 정의하고 다음과 같이 출력한다.
myList1 : ['홍길동', '신데렐라', '알라딘', '장화', '홍련',
'지니', '엘리스']
myList2 : ['토끼', '거북이', '물개', '펭귄']
2개의 리스트 합 : (결과값 출력)
4개만 출력 :(결과값 출력)
짝수번째만 출력 : (결과값 출력)
홀수번째만 출력 : (결과값 출력)
총 길이 :11
'''

myList1 = ['홍길동', '신데렐라', '알라딘', '장화', '홍련',
'지니', '엘리스']
myList2 = ['토끼', '거북이', '물개', '펭귄']
print(myList1)
print(myList2)
print(myList1+myList2)
print(myList1[0:4])
print(myList1[1:8:2]+myList2[1:5:2])
print(myList1[0:8:2]+myList2[0:5:2])
print(len(myList1+myList2))

# 퀴즈
'''
리스트를 정의한 후 리스트 요소를 편집한다.(변경, 삭제, 추가)
['사과', '배', '망고']
첫번째 요소 변경 후 : ['포도', '배', '망고']
마지막 위치에 요소 추가후 : ['포도', '배', '망고', '오렌지']
2번째 위치에 요소 추가후 : ['포도', '수박', '배', '망고', '오렌지']
마지막 위치 삭제 : ['포도', '수박', '배', '망고']
배 삭제 : ['포도', '수박', '망고']
'''

fruits = ['사과','배','망고']
print(fruits,type(fruits))
fruits[0]='포도'
fruits.append('오렌지')
fruits.insert(1,'수박') # 리스트에 insert 는 순서 , 문자 모두 입력
fruits.remove('오렌지')
fruits.remove('배')
print(fruits)

# 퀴즈
'''
데이터를 입력받은 후 리스트에 추가하는 예제입니다.
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 쥬라기 공원
좋아하는 가수는? 케이윌
당신에 관한 리스트 : ['초밥', '쥬라기 공원', '케이윌']
'''

myList = []
food = input('좋아하는 음식은 ?')
movie = input('최근 본 영화는 ?')
singer = input('좋아하는 가수는 ?')
myList.append(food)
myList.append(movie)
myList.append(singer)
print(myList)

# 퀴즈
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스'] 
동생이 사과 를 먹었다
우리집 냉장고에는?  ['망고', '치즈케이크', '주스'] 
이모가 수박을 사오셨다.
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박'] 
동생 친구가 치즈케이크,수박을 먹었다.
우리집 냉장고에는?  ['망고', '주스'] 
'''

foods = ['사과','망고','치즈케이크','주스']
foods.remove('사과')
foods.append('수박')
foods.remove('치즈케이크')
foods.remove('수박')
print(foods)

# 퀴즈
'''
아래의 리스트를 이용하여
grade 2차원 리스트를 만들고
총점과 평균을 과목별로 출력한다.

kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]

grade = [[ 55, 66, 34, 60],[ 78, 90, 45, 88],
[56, 98, 78, 90]]

kor = 총점(), 평균()
math = 총점(), 평균()
eng = 총점(), 평균()
'''

kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]

grade =list([kor] + [math] + [eng])
print(grade)
K = kor[0]+kor[1]+kor[2]+kor[3]
M = math[0]+math[1]+math[2]+math[3]
E = eng[0]+eng[1]+eng[2]+eng[3]
print(K)
print(M)
print(E)
print('kor = 총점 {}, 평균 {}'.format(K, K/4))
print('math = 총점 {}, 평균 {}'.format(M, M/4))
print('eng = 총점 {}, 평균 {}'.format(E, E/4))

# 퀴즈
'''
아래와 같이 튜플을 정의한 후 출력한다.

튜플 리스트 : ('강아지','토끼','돼지','곰')

튜플 요소 추가 후 : ('강아지','토끼','돼지','곰','호랑이')

튜플의 0-3번쨰 요소표시 : ('강아지','토끼','돼지')

'강아지' 요소의 위치값은 ?

튜플을 문자열로 변환하여 출력 : 강아지,토끼,돼지...

튜플을 리스트로 변환하여 출력
'''

myTuple = ('강아지','토끼','돼지','곰')
myTuple += ('호랑이',) # 요소 하나만 추가할때 , 빼먹지않기 !
print(myTuple,type(myTuple))
print(myTuple[:3])
print(myTuple.index('강아지'))
myStr = str(myTuple)
myList = list(myTuple)
print(myStr,type(myStr))
print(myList,type(myList))

