# 비교연산자 
# True / False 리턴
a = 1
b = 1
print(a == b)


# 논리 연산자
# or 연산자는 둘중에 하나만 True 이면 True
# T or T = > T
# T or F = > T
# F or T = > T
# F or F = > F

a = 1
b = 10
print((a==1) or (b==3))
print( (a==51) or (b==13) )

# and 연산자는 모두 True 여야만 True
# T and T = > T
# T and F = > F
# F and T = > F
# F and F = > F

a = 1
b = 10
print((a==1) and (b==3))
print( (a==1) or (b==10) )

# not 연산자는 True/False 반대값을 리턴
# not T -> F

a = 1
print( not(a==1) )
print( not(a==10) )

# if 문
# if True:
#    실행할 문장

# 무조건 실행
if True:
    print('조건제어문')


#
a = 1
b = 10
if a>b: # False
    print('a는 b보다 크다.')

if a<=b: # True
    print('a는 b보다 작다.')

# 조건식에서 True가 되는 조건 = True, 0빼고 나머지 숫자
# 조건식에서 False가 되는 조건 = False, 0, '', None
money = 0 # False
if money :
    print('택시를 타고')
print(' 가자 ')

print('-'*30)
money = 1 # True
if money :
    print('택시를 타고')
print(' 가자 ')

print('-'*30)
money = '' # False
if money :
    print('택시를 타고')
print(' 가자 ')

print('-'*30) # False
money = None
if money :
    print('택시를 타고')
print(' 가자 ')

'''
퀴즈 - 입력받은 값에 따라 양수 , 음수 출력하기
'''
data = int(input('정수를 입력해주세요 ... '))
if data<0:
    print('음수')

if data>0:
    print('양수')

if data==0:
    print('0')

'''
퀴즈 - 나이를 입력받은후 19세 이상이면 '당신은 성인입니다'
'''

data1 = int(input('당신의 나이는 어떻게 됩니까 ?'))
if data1>=19:
    print('당신은 성인입니다.')
if 17<= data1 <19:
    print('당신은 고등학생 입니다.')
if 14<= data1 <17:
    print('당신은 중학생 입니다.')
if data1 <= 13:
    print('당신은 초등학생이하 입니다.')

    # 퀴즈
    '''
    입력받은 숫자 값이 짝수이면 숫자 : 짝수
    홀수이면 숫자 : 홀수
    
    숫자%2 == 0 짝수
    숫자%2 != 0 홀수
    '''

myNum = int(input('정수로 된 숫자를 입력해주세요 ...'))
if myNum % 2 == 0:
    print(myNum,' : 짝수 ')
if myNum % 2 != 0:
    print(myNum , ' : 홀수 ')

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

print('-'*30)
k = float(input('당신의 키는 몇m 입니까?'))
w = float(input('당신의 몸무게는 몇 kg 입니까?'))
k2 = k**2 # k2 = k의제곱
bmi = w/k2

print('bmi = %4.2f' % bmi) 

# 소수점 자리수 표시하기
# xx.xx : 4.2f =>전체자리수 . 소수점자리수
# 12.56789 : 4.2f -> 12.56

if bmi >35:
    print(' 당신은 고도 비만 입니다. ')
    
if 30 <= bmi <35:
    print(' 당신은 중등도 비만 입니다. ')
    
if 25 <= bmi < 30:
    print(' 당신은 경도 비만 입니다. ')

if 23 <= bmi < 25 :
    print(' 당신은 과체중 입니다. ')

if 18.5 <= bmi < 23:
    print(' 당신은 정상 입니다. ')

if bmi < 18.5:
    print(' 당신은 저체중 입니다. ')

# 퀴즈
'''
Animal = 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양

띠 = 태어난년도%12
'''
year = int(input('당신은 몇년도에 태어나셨습니까? '))
animal = year%12
if animal == 0 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'원숭이'))

if animal == 1 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'닭'))

if animal == 2 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'개'))

if animal == 3 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'돼지'))

if animal == 4 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'쥐'))

if animal == 5 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'소'))

if animal == 6 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'호랑이'))

if animal == 7 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'토끼'))

if animal == 8 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'용'))

if animal == 9 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'뱀'))

if animal == 10 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'말'))

if animal == 11 :
    print('당신이 태어난 년도는 {} 년이고 당신은 {}띠 입니다'.format(year,'양'))


    