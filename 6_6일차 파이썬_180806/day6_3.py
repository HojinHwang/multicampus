# 예외처리
# 에러가 발생했을 경우 어떻게 처리해야 하는가 ?

# 에러가 나는 경우
# 0으로 나누는 경우

# print(10/0)
# ZeroDivisionError: division by zero

# 리스트, 튜플 구조에서
# index가 없는 경우
myList=[1,2,3]
# print(myList[3]) 
# IndexError: list index out of range

# 파일 오픈 에러
# f = open('none.txt','r')
# print(f.read())
# FileNotFoundError: 
# [Errno 2] No such file or directory: 'none.txt'

# 문법
# try:
#   실행할 명령
# except 에러코드 as e :
#   실행할 명령

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 에러 무시
# pass 명령 이용
print('-'*40) 
try:
    4 / 0
except ZeroDivisionError as e:
    pass # 위의 에러가 발생하면 그냥 무시하라

print('오류 무시')

myList=[1,2,3]
try:
    print(myList[3]) 
except IndexError as e:
    print(e,'가 발생하였습니다.')

try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    f.close()

# try:
#   명령 실행1
# except 오류 as e:
#   명령 실행2
# else:
#   명령 실행3
# finally:
#   명령 실행4

try:
    f = open('data/Yesterday.txt','r')
except FileNotFoundError as e:
    print(e)
else:
    print(' 존재하는 파일입니다. ')
    f.close()

try:
    4 / 0
except ZeroDivisionError as e:
    print('0으로 나누면 생기는 에러')
finally:
    print('수행 완료')

# 퀴즈
'''
2개의 숫자 값을 입력받은 후
나누기한다.
에러가 발생을 하면
    '에러가 발생했습니다.' 출력
에러가 발생 안하면
    숫자1 나누기 숫자2 = 결과값
'''

n1 = int(input('숫자1 = ?'))
n2 = int(input('숫자2 = ?'))

try:
    n1/n2
except ZeroDivisionError as e:
    print('에러가 발생했습니다.')
else:
    print('{} / {} = {}'.format(n1,n2,n1/n2))



