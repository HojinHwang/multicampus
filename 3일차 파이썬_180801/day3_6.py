# 반복문 : while
# while 조건:
#       실행명령

# 무한 루프
# while True:
#    print('Python')

# while 조건:
#       실행명령
#       False 조건

# 초기값
# while False가 될 조건 제시:
#       증감
#       실행명령
#
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다')




# 퀴즈 - 10....1 까지 출력
num = 10
while num >0:
    print(num)
    num -= 1
    # num = num - 1

# 퀴즈 - 다음과 같이 출력
'''
*
**
***
****
*****
'''


num = 1
while num <6:
    print('*'*num)
    num += 1

# 퀴즈2 - 다음과 같이 출력
'''
*****
****
***
**
*
'''

num = 5
while num>0:
    print('*'*num)
    num -= 1

# 퀴즈
# 1~50까지 합 구하기
n = 1
sum = 0
while n <51:
    n += 1
    sum += n
    print(' 1~50까지의 합 =',sum) 

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

digit = int(input('정수값으로 입력하세요?'))
n = 1
while n <= 9:
    print( ' {} X {} = {}'.format(digit,n,digit*n))
    n += 1

print('*'*10)
digit = int(input('정수값으로 입력하세요?'))
n = 1
while n <= 9:
    if digit*n <10:
        print( ' {} X {} = {} '.format(digit,n,digit*n))
    else:
        print( ' {} X {} = {} '.format(digit,n,digit*n))
        n += 1


# while + break
# 무한루프를 빠져나갈 경우 break문 이용
# while True조건 :
# if 블록을 빠져나갈 조건:
#    break


#while True:
#    ans = input('아무값이나 입력하세요.')
#    if ans == 'x':
#        break
# print(' 입력종료 ')

coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee -= 1
    print('남은 커피의 양은 {}개입니다'.format(coffee))
    if not coffee:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break

# 퀴즈
# 입력값을 리스트요소로 추가
myList = []
print(' 리스트 입력 시작 ')
while True:
    data = input( ' 종료시 x ....? ')
    myList.append(data)
    if data == 'x':
        break
print('리스트 입력 종료')
print('리스트 - ',myList)

