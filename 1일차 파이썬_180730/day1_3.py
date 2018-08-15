# 대입 연산자

a = 10
b = 10
print(a,b)
a += 10 # a=a+10
b += 5 # b=b+5
print(a,b)

a = 0
a += 10
print('a += 10', a)
a -= 5
print('a -= 5', a)
a *= 10
print('a *= 5', a)
a /= 2
print('a /= 2', a)

# 관계 연산자
# == 같다
# != 같지 않다

print(10 == 10)
print(10 != 10)

# 연산자 우선순위
'''
괄호()
*, /
+, -
'''
print(100+20*40)
print((100+20)*40)

# .format()을 이용한 출력

print( '{a} {b} '.format(a=12, b=33))

a = 10
b = 5

print('a = {}, b = {}'.format(a,b))
# print('a + b = ' , a+b)
print(' 덧셈 - a + b = {}'.format(a+b))
print(' 곱셈 - a * b = {}'.format(a*b))

# 퀴즈
# 2개의 숫자를 입력받아
# 사칙연산의 결과물을 format() 함수를 이용해서 출력하여라
'''
첫번째 숫자를 입력하세요 ? 34
두번째 숫자를 입력하세요 ? 56

결과 :
34 + 56 =
34 - 56 =
34 * 56 =
34 / 56 =

'''

a = int(input(' 첫번째 숫자를 입력하세요 ?'))
b = int(input(' 두번쨰 숫자를 입력하세요 ?'))

print(' {} + {} = {}'.format(a,b,a+b))
print(' {} - {} = {}'.format(a,b,a-b))
print(' {} * {} = {}'.format(a,b,a*b))
print(' {} / {} = {}'.format(a,b,a/b))

print( '%d %d' % (100,200))

# %를 이용한 출력
# print('%d %f %s' % (정수 , 실수 , 문자열))
myName = 'Jhon'
print('Name : %s ' % (myName))
num1 = 12.34
print(' num1의 값 : %f ' % (num1))
num2 = 12
print(' num2의 값 : %d ' %(num2))

# 퀴즈 : % 기호를 이용하여 출력하여라
a = int(input(' 첫번째 숫자를 입력하세요 ?'))
b = int(input(' 두번쨰 숫자를 입력하세요 ?'))

print(' {} + {} = {}'.format(a,b,a+b))
print(' {} - {} = {}'.format(a,b,a-b))
print(' {} * {} = {}'.format(a,b,a*b))
print(' {} / {} = {}'.format(a,b,a/b))

print('%d + %d = %d ' % (a,b,a+b))
print('%d - %d = %d ' % (a,b,a-b))
print('%d * %d = %d ' % (a,b,a*b))
print('%d / %d = %d ' % (a,b,a/b))

# % 는 출력을 어떻게 하나요?
# rate = 12.90 %
rate = 12.90
print('%f 퍼센트(%%) ' % (rate))

# 문자열 인덱싱 
# : 0부터 시작한다.
# : 음수값 지정시 뒤에서 부터 위치가 지정된다.
# 문자열 안의 위치

myString = 'Python'
print(' 1 번째 위치 문자 = ',myString[0] ) #P
print(' 3 번째 위치 문자 = ',myString[2] ) #t
print(' 마지막 위치 문자 = ',myString[5] ) #n
print(' 마지막 위치 문자 = ',myString[-1] ) #n
print(' 문자열의 끝에서 두번째 문자 = ',myString[-2] ) #o

# 문자열 슬라이싱 - 부분 추출
# 문자열변수[start:end:step]
# Shift + Enter 하면 부분실행 가능
myString = 'Python Program'
print(myString[0:3]) #Pyt
print(myString[:6]) #Python
print(myString[5:]) #n Program
print(myString[::2]) #Pto rga

# 퀴즈
# 슬라이싱 기능을 이용하여 다음과 같이 출력한다
'''
Before : Life is too short , You need Python
After : Life Pytho
'''
strTest = 'Life is too short, You need Python'
print('Before : ',strTest)
print('After : ', strTest[:4],strTest[-7:-1])
print(strTest[0:5] + strTest[-6:-1])

# 퀴즈 - p106 - 01 , 02
pin = '881120-1068234'
print('yyyymmdd = ', pin[:6])
print('number = ' , pin[-7:] )
print('sex = ',pin[7])