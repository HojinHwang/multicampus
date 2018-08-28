#

# 퀴즈
'''
입력받은 값 n으로 1~n 까지의 합계찍기에 관련된 함수를 정의하고
결과를 출력한다.

10을 입력받았다면 ?

1~10 의 합 : ?
1+2+...+10
'''
print('퀴즈1')

def sumPlus(m):
    sum = 0
    for i in range(m+1):
        sum += i
    print('1~ {} 까지의 합 : {}'.format(m,sum))

m = int(input(' 정수 입력 ? ...'))
sumPlus(m)




# 퀴즈2
'''
3개의 인자값을 입력받은 후
첫번째 인자값에 따라 사칙 연산하기

첫번째 인자값이 c1 이라면 ?
cal(c1,2,3) - 더한다   5
cal(c2,2,3) - 뺀다    -1
cal(c3,2,3) - 곱한다   6
'''

def Calculator(choice,n,m):
    print('입력값 :', choice,n,m)
    if choice == 'c1':
        return '더한다',n+m
    elif choice == 'c2':
        return '뺀다', n-m
    elif choice == 'c3':
        return '곱한다',n*m
    elif choice == 'c4':
        return '나눈다',n/m 
    else:
        return '입력오류'   

print(Calculator('c1',10,5))
print(Calculator('c2',10,5))
print(Calculator('c3',10,5))
print(Calculator('c4',10,5))