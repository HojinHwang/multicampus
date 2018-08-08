# 튜플(Tuple)
# 튜플 구조 정의 1
# 튜플이름 = (아이템값1, ....)
t1 = ('도','레','미','파','솔')
print(t1,type(t1))

# 튜플 구조 정의 2
# 튜플이름 = 아이템값1, 아이템값2 ..
t2 = 1,2,3,4,5
print(t2,type(t2))

# 튜플 인덱싱
# 튜플이름[위치번호] 0번부터 시작
t1 = ('도','레','미','파','솔')
print(t1)
print(t1[0])
print(t1[-1])
# 튜플 슬라이싱
print(t1[0:3])

# 튜플의 편집방식
# 삭제 , 변경은 불가능
# 추가 가능
myTuple = (100, '강아지', '지렁이')
print('myTuple = ',myTuple)
print('myTuple[0] = ', myTuple[0])
# myTuple[0] = 200 변경 불가
# 추가 가능
# 튜플이름 += (값1,값2...)
# 튜플 요소 하나만 추가할 경우
# 튜플이름 += (값,)  - > 뒤에 ,를 찍어줘야함
myTuple += (50,100)
print('myTuple = ', myTuple)
myTuple += ('끝',)
print('myTuple = ',myTuple)

# 튜플함수 적용
# 요소의 반복값 확인
# 튜플이름.count(요소값) -> 정수
t1 = (100,50,30,30,30)
print('30의 반복 횟수 : ',t1.count(30))
# t1.sort() 불가능
# 튜플 전체의 길이 = 요소의 총 갯수
# len(튜플이름))
print(len(t1))

# 튜플 요소의 위치값 반환
# 튜플이름.index(요소값)
print(t1.index(30))


# 자료구조 변환

# 문자열 => 튜플
# tuple(문자열변수나 문자열)
myStr = 'Python'
print(myStr, type(myStr))
myTuple = tuple(myStr)
# ('P', 'y', 't', 'h', 'o', 'n')
print(myTuple,type(myTuple))

print('-'*20)
# 리스트 => 튜플
# tuple(리스트이름)
myList = ['수학','과학','영어']
print(myList, type(myList))
myTuple = tuple(myList)
print(myTuple, type(myTuple))

# 튜플 -> 리스트
# list(튜플이름 )
myTuple = (100,50,30,30,30)
myList = list(myTuple)
print(myList, type(myList))

# 튜플 => 문자열 1
# str(튜플이름)
myTuple = ('도','레','미','파','솔')
print(myTuple, type(myTuple))
myStr = str(myTuple)
print(myStr, type(myStr))
print(myStr[0]) # (

# 튜플 => 문자열 2
# '구분자'.join(튜플이름)
myTuple = ('도','레','미','파','솔')
print(myTuple, type(myTuple))
# 도,레,미,파,솔
myStr = ','.join(myTuple)
print(myStr, type(myStr))
myStr2 = '/'.join(myTuple)
print(myStr2, type(myStr2))

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
print('-'*40)
t1 = ('강아지','토끼','돼지','곰')
print(t1)
t1 += ('호랑이',)
print(t1, type(t1))
print(t1[0:4])
print(t1.index('강아지'))
Strt1 = str(t1)
print(Strt1, type(Strt1))
Strt2 = ','.join(t1)
print(Strt2, type(Strt2))
t1 = ('강아지','토끼','돼지','곰')
Listt1 = list(t1)
print(Listt1, type(Listt1))





