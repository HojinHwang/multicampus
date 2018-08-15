# 기본 자료형
# 숫자형(정수,실수), 문자열(인용부호 이용해서 정의)
# 논리형 - True / False

print(10>0) #True
print(10<0) #False

# 관계 연산자란 ?
# > , <, >=, <=, ==,
print(10 == 0) # False

# type()
# 자료형 출력하기
print(type(' Python '))
print(type(True))
print(type(2))
print(type(1.23))

# 캐스팅 : 형 변환
# 숫자 -> 문자 str(값))
print(1) #정수
print(type(1)) #<class 'int'>
print(str(1)) # 문자열
print(type(str(1))) # <class 'str>
# 문자 -> 정수 숫자 int(값)
print('123')
print(type('123')) # <class 'str'>
print(int('123'))
print(type(int('123')))
# 정수 -> 실수 float(값)
print(500)
print(float(500))

# 입력문
# 입력받은 값의 데이터형은 문자형
#inData = input('숫자를 입력하세요? ')
#print(' 입력한 숫자는 \n', inData, '입니다.')
#print(type(inData))

# 입력받은 2개의 숫자를 더해라
#num1 = input(' 숫자 1 ? ')
#num2 = input(' 숫자 2 ? ')
#print(' num1 =', num1)
#print(' num2 =', num2)
#print(' num1 + num2 = ', int(num1)+int(num2)) #숫자로 변경해서 더한 값

# 퀴즈
# 2개의 숫자를 입력받아서 사칙연산의 결과물을 출력하여라.
'''
첫번째 숫자를 입력하세요 ? 34
두번째 숫자를 입력하세요 ? 56

결과 :
34 + 56 =
34 - 56 =
34 * 56 =
34 / 56 =

'''

n1 = input('첫번째 숫자를 입력하세요 ?')
n2 = input('두번째 숫자를 입력하세요 ?')
print('34 + 56 =',int(n1)+int(n2))
print('34 - 56 =',int(n1)-int(n2))
print('34 * 56 =',int(n1)*int(n2))
print('34 / 56 =',int(n1)/int(n2))

