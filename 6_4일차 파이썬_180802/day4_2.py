# 함수(function)

# 함수란?
# 명령문의 조합
# 함수 < 클래스 < 모듈 < 패키지

# 함수정의 문법
'''
def 함수이름():
    명령문
    ... 
    return 문
'''
# 함수의 종류
# 인자 x, 결과값 x
# 인자 o, 결과값 x
# 인자 o, 결과값 o





# 인자도 없고 return 문도 없음
# python 글자를 3번 출력하는 함수 정의

def printPy():
    print('Python'*3)

# 함수 호출
printPy()

# 인자는 있고 return 문이 없음
# 2개의 숫자를 합해서 출력하는 함수 정의

def sum(n1,n2):
    print(' {} + {} = {} '.format(n1,n2,n1+n2))

sum(12,34)
sum(12,34)
sum(12,34)

# 인자도 있고 return 문도 있음.
# 두개의 숫자를 받아서 빼서 출력하는 함수
# 결과값만 리턴하는 함수

def minus(n1,n2) :
    return n1-n2

result = minus(100,50)
print(result)


'''
퀴즈: 인자값을 받아서 구구단을 출력하라.
'''

def gugu(n):
    print('*'*30)
    for i in range(1,10):
        print(' {} X {} = {}'.format(n,i,n*i))

gugu(9)
gugu(6)

# 결과값이 다중인 함수
def sum_mul(n1,n2):
    return n1+n2, n1*n2

print(sum_mul(3,5))
result = sum_mul(3,5)
print(type(result)) # <class 'tuple'>

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

# 키와 몸무게를 인자로 입력하여 메세지가 출력되도록 한다.
def bmi(k,w):
    return w / (k**2/100)
bmi(170,60)
