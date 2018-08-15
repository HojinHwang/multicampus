# 퀴즈 
'''
딕셔너리 구조로 차:브랜드 형태로 5개만 정의 
예) '레이':'기아'

딕셔너리 요소 추가 - 총6개 
딕셔너리 요소 삭제 - 총4개 
딕셔너리 마지막 요소의 값만 호출 
딕셔너리 구조에서 키값만 출력 
딕셔너리 구조에서 실제값만 출력 

'''

mydict = {'레이':'기아','소나타':'현대','말리부':'GM',
'R8':'아우디','베라크루즈':'현대'}
print(mydict,type(mydict))
mydict['티구안'] = '폭스바겐'
print(mydict)
del mydict['레이']
del mydict['소나타']
print(mydict)
print(mydict['티구안'])
print(mydict.keys())
print(mydict.values())

# 퀴즈
'''
입력받은 값에 따라 양수 , 음수 출력하기
'''

data = int(input('정수를 입력해주세요 ... '))
if data > 0:
    print('양수')
if data < 0:
    print('음수')
else:
    print('0이다.')

# 퀴즈
'''
나이를 입력받은후 19세 이상이면 '당신은 성인입니다'
'''

age = int(input('당신의 나이는 몇입니까 ?'))
if age >= 19:
    print('당신은 성인입니다.')
if age < 19:
    print('당신은 성인이 아닙니다.')

 # 퀴즈
    '''
    입력받은 숫자 값이 짝수이면 숫자 : 짝수
    홀수이면 숫자 : 홀수
    '''

number = int(input('숫자값을 입력하세요.'))
if number%2 == 0 :
    print('짝수입니다.')
if number%2 == 1 :
    print('홀수입니다.')

# 퀴즈 1
'''
bmi 값에 따라 출력한다.

k = 키(입력값) 단위 
w = 체중(입력값)

bmi = 체중(kg)/키(m)의제곱
키**2 = 제곱

bmi 값에 따라 다음과 같이 출력한다.

고도 비만 : 35 이상
중등도 비만 : 30 - 35
경도 비만  : 25 - 30
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
'''

k = float(input('당신의 키는 몇입니까?'))
w = float(input('당신의 몸무게는 몇입니까?'))
k2 = k**2
bmi = w/k2

if bmi >= 35:
    print('고도 비만입니다.')
if 30 <= bmi < 35:
    print('중등도 비만입니다.')
if 25 <= bmi < 30:
    print('경도 비만입니다.')
if 23 <= bmi < 25:
    print('과체중입니다.')
if 18.5 <= bmi < 23:
    print('정상입니다.')
if bmi < 18.5:
    print('저체중입니다.')

# 퀴즈
'''
Animal = 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양

띠 = 태어난년도%12
'''
Year = int(input('당신은 몇년도에 태어나셨습니까 ?'))
Animals = '원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양'
Animal = Year % 12
print(Year)
print(Animal)
if Animal == 0:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[0]))
if Animal == 1:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[1]))
if Animal == 2:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[2]))
if Animal == 3:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[3]))
if Animal == 4:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[4]))
if Animal == 5:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[5]))
if Animal == 6:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[6]))
if Animal == 7:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[7]))
if Animal == 8:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[8]))
if Animal == 9:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[9]))
if Animal == 10:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[10]))
if Animal == 11:
    print('당신은 {}년도에 태어났고 {}띠 입니다.'.format(Year,Animals[11]))

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

score = float(input('학점을 입력하세요.'))
if score == 4.5 :
    print('신')
if 4.2 <= score < 4.5 :
    print('교수님의 사랑')
if 3.5 <= score < 4.2 :
    print('현 체제의 수호자')
if 2.8 <= score < 3.5 :
    print('일반인')
if 2.3 <= score < 2.8 :
    print('일탈을 꿈꾸는 소시민')
if score < 2.3 :
    print('시대를 앞서가는 혁명의 씨앗')

# 퀴즈 - 다음과 같이 출력
'''
*
**
***
****
*****
'''

a = 1
while a <= 5:
    print('*'*a)
    a += 1

# 퀴즈
# 1~50까지 합 구하기

n = 0
sum = 0
while n <= 50:
    n += 1
    sum += n
    print(sum)

# 퀴즈 2
# 구구단 출력할 단수를 입력한 후
# 입력값에 대한 구구단을 출력한다.
# 정수값으로 입력하세요 ? 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# ...

n = int(input('정수값으로 입력하세요 ?'))
i = 1
while i <= 9:
    if n*i < 10:
        print('{} X {} = {}'.format(n,i,n*i))
    else:
        print('{} X {} = {}'.format(n,i,n*i))
    i += 1

# 퀴즈
coffee = 10
money = 300
while money:
    print('커피를 줍니다.')
    coffee -= 1
    print('남는 양의 커피는 {}개 입니다.'.format(coffee))
    if not coffee:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다')
        break

# 퀴즈
# 입력값을 리스트요소로 추가
myList = []
print('리스트 입력 시작')
while True:
    data = input('종료시 x...?')
    myList.append(data)
    if data == 'x':
        break
print('리스트 입력 종료')
print(' 리스트 :', myList)
    
    

