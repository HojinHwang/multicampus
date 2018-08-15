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

a1 = int(input('첫번째 숫자를 입력하세요 ?'))
a2 = int(input('두번째 숫자를 입력하세요 ?'))
print('{} + {} = {}'.format(a1,a2,a1+a2))
print('{} - {} = {}'.format(a1,a2,a1-a2))
print('{} * {} = {}'.format(a1,a2,a1*a2))
print('{} / {} = {}'.format(a1,a2,a1/a2))

# 퀴즈 2
# 슬라이싱 기능을 이용하여 다음과 같이 출력한다

'''
Before : Life is too short , You need Python
After : Life Pytho
'''

answer = 'Life is too short , You need Python'
print(answer[:4] + answer[-6:-1])

# 퀴즈 - p106 - 01 , 02
pin = '881120-1068234'
print('yymmdd = {}'.format(pin[:6]))
print('number = {}'.format(pin[-7:]))
print('sex = {}'.format(pin[7]))