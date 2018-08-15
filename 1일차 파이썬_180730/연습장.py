# 연습장
food = "python's favorite food is ferl"
print(food)
multiline = "Life is too short\nYou need python"
print(multiline)
head = 'Hojin'
tail = ' is handsome'
print(head + tail)
print(head*2)
a = 'Python is fun'
print(a[0:6])

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
n1 = int(input('첫번째 숫자를 입력하세요 ?'))
n2 = int(input('두번째 숫자를 입력하세요 ?'))
print(' n1 = {}, n2 = {}, n1 + n2 = {}'.format(n1,n2,n1+n2))
print(' n1 = {}, n2 = {}, n1 - n2 = {}'.format(n1,n2,n1-n2))
print(' n1 = {}, n2 = {}, n1 * n2 = {}'.format(n1,n2,n1*n2))
print(' n1 = {}, n2 = {}, n1 / n2 = {}'.format(n1,n2,n1/n2))
'''
위랑 같은 값들을 가지는 다른 식
'''
print(' %d + %d = %d '%(n1,n2,n1+n2))




