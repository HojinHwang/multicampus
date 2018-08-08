# if ~ else (2가지에서 택일)
# if 조건문:
#    참일때 실행할 명령문
# else:
#     거짓일때 실행할 명령문

# money = 0 #False

money = 1500
if money :
    print('택시를 타고 가라.')
else:
    print('걸어 가라')
    print('----------------------끝')

myNum = int(input('정수로 된 숫자를 입력해주세요 ...'))
if myNum % 2 == 0:
    print(myNum,' : 짝수 ')
else:
    print(myNum , ' : 홀수 ')

# if ~ elif ~ else (여러가지 조건에서 택일)
# if 조건1:
#    조건1이 참일때 실행할 명령문
# elif 조건:
#    조건2가 참일때 실행할 명령문
# else:
#     거짓일때 실행할 명령문

# 3가지 조건 (음수, 0, 양수)
myNum = 0

if myNum > 0:
    print('양수')
elif myNum < 0:
    print('음수')
else :
    print('0')

data1 = int(input('당신의 나이는 어떻게 됩니까 ?'))
if data1>=19:
    print('당신은 성인입니다.')
elif 17<= data1 <19:
    print('당신은 고등학생 입니다.')
elif 14<= data1 <17:
    print('당신은 중학생 입니다.')
else:
    print('당신은 초등학생이하 입니다.')


# in 연산자
# 결과값이 True / False
# item in Group

# 문자가 문자열에 있는가?
print('a' in 'banana') # True
print('p' in 'banana') # False

# 아이템이 리스트에 있는가?
userName = ['홍길동','김삿갓','트와이스']
print('김삿갓' in userName) # True
print('신데렐라' in userName) # False

# 아이템이 튜플에 있는가?
userName = ('홍길동','김삿갓','트와이스')
print('김삿갓' in userName) # True
print('신데렐라' in userName) # False

# 아이템이 집합안에 있는가?
userName = {'홍길동','김삿갓','트와이스'}
print('김삿갓' in userName) # True
print('신데렐라' in userName) # False

# not in 연산자
# 결과값이 True / False
# item not in Group
# 아이템이 그룹안에 없을경우 True
# 아이템이 그룹안에 있을경우 False

print('a' not in 'banana') # False
print('p' not in 'banana') # True

# 아이템(요소)이 리스트에 없으면 True
userName = ['홍길동','김삿갓','트와이스']
print('김삿갓' not in userName) # False
print('신데렐라' not in userName) # True


# if문에 in 연산자 사용하기
myList = ['바나나', '포도', '수박']
if '바나나' in myList:
    print('바나나가 리스트에 있다.')
else :
    print('바나나가 리스트에 없다.')

myWay = ['bus', 'subway', 'taxi']
myStats = 0

if 'my Car' in myWay:
    print('내 차를 타고 간다.')
elif myStats:
    print('버스를 타고 간다.')
elif 'subway' not in myWay:
    print('지하철을 타고 간다.')
elif 'school bus' not in myWay:
    print('스쿨 버스를 타고 간다.')
else:
    print('걸어간다.')


# 퀴즈
# 학점을 입력받아서 메세지 출력
'''
변수를 선언합니다.
score = float(input('학점 입력> '))

score = 4.5 : 신
4.2 <= score < 4.5 : 교수님의 사랑
3.5 <= score < 4.2 : 현 체제의 수호자
2.8 <= score < 3.5 : 일반인
2.3 <= score < 2.8 : 일탈을 꿈꾸는 소시민
score < 2.3 : 시대를 앞서가는 혁명의 씨앗
'''

score = float(input('학점 입력 ='))
if score == 4.5:
    print('신')
elif 4.2 <= score < 4.5:
    print('교수님의 사랑')
elif 3.5 <= score < 4.2:
    print('현 체제의 수호자')
elif 2.8 <= score < 3.5:
    print('일반인')
elif 2.3 <= score < 2.8:
    print('일탈을 꿈꾸는 소시민')
else:
    print('시대를 앞서가는 혁명의 씨앗')
    
    
    


