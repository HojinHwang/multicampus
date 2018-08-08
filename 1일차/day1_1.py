# 주석
# 설명글이다.
'''
여러줄 주석 인용부호
'''
# 문자열 출력
# 문자열은 '~' , "~"
# print(문자열)
# print(문자열1,문자열2 ... )
print( "hello python1" )
print( "hello python2" )
print( "hello python3" )
print( 'hello python1', 'hello python2', 'hello python3')
# 문자열 연산자 : 자료형이 같아야 한다.
# + 연결
# * 반복
print(' 파이썬 '*3)
print(' 파이썬 '+'프로그래밍')
# print('파이썬'+ 123) # TypeError
print(' 파이썬 '+ '123')
# 문자열 길이 확인
# len(문자열)
print('문자열 길이 확인 : ',len('abcdefg'))

#이스케이프 문자
# \n 줄바꿈
# \t 탭. 왼쪽 여백 생성
# \'' 인용부호 출력
# \"" 인용부호 출력

print('안\n녕\n\n\n')
print('\t안\t녕')
print('\"안녕\"')

print(' + 연산자' , 100+100)
print(' - 연산자' , 100-10)
print(' * 연산자', 100*100)
print(' / 연산자', 100/10)
print(' // 연산자', 100//3)
print(' % 연산자',100%3)
# //은 정수로 나타냄 소수점 없음.

print('-'*30)
print('5+5=', 5+5)
print('6*6=', 6*6)
print('10-3=', 10-3)
print('100 나누기 3의 나머지는 ?', 100%3)
print('-'*30)
# print(' ') 이부분은 문자로 해석된다
# 퀴즈 :
# 아래와 같이 3줄로 글자를 출력하는 3가지 방법
'''
파이썬
파이썬
파이썬
'''
# 방법 1
print('파이썬\n파이썬\n파이썬\n')
# 방법 2
print('파이썬\n'*3) # best
# 방법 3
print('파이썬')
print('파이썬')
print('파이썬')