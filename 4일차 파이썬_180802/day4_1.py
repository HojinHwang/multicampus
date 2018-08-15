# Continue 문

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:continue
    print(a) # 홀수

print('-'*30)
a = 0
while a < 10:
    a += 1
    if a % 2 == 1:continue
    print(a) # 짝수


b = 0 
while b < 10:
    b += 1
    if b == 5:continue
    print(b) # 5 빼고 1~10

range(10)

myList = list(range(5,11)) # 5,6,7,8,9,10
print(myList)

myList = list(range(0,20,2)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(myList)

myList = list(range(3,30,3)) # [3, 6, 9, 12, 15, 18, 21, 24, 27] 
print(myList)

sum = 0
for i in range(1,11):
    sum = sum + i
    print(sum)

for i in range(0,21,2):
    if i == 0: # 0이면 입력 x
     pass
    else:
     print(i,'\t',end ='') # 왼쪽 공백 , 가로줄에 다 쓰이게 함

myList = [1,2,3]
for i in myList:
    print(i)

myTurple = (1,2,3)
for i in myTurple:
    print(i)

# for 변수 in 리스트,튜플,문자열,range(start,end,step):
#    실행 명령

# 3번만 명령 실행
# 1 Hello
# 2 Hello
# 3 Hello
for i in range(1,4):
    print(i ,'Hello')

cnt=1
for i in ['a','b','c']:
    print('요소 {} : {}'.format(cnt,i))
    cnt += 1

mytuple = ('과자','라면','김밥')
for t in mytuple:
    print(t,end='')
# print()
print('\n','-'*30)

# 리스트에서 최대값 출력
myList = [50,44,100,30,1]
result = myList[0] # 50
for i in myList:
    if result <i:
        result = i
print('최대값 : ',result)

# 리스트에서 최소값 출력
myList = [50,44,100,30,1]
result = myList[0] # 50
for i in myList:
    if result >i:
        result = i
print('최소값 : ',result)

# 중첩 for 문
for i in range(5):
    print(i)
    for j in range(3):
        print(j,'****')
    print('-'*30)

# 퀴즈 : 구구단 찍기
'''
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
'''
'''
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
'''

for i in range(2,10):
    print('*'*20)
    for j in range(1,10):
        # print(' {} X {} = {}'.format(i,j,i*j))
        if i*j < 10:
            print(' {} X {} = {}'.format(i,j,i*j))
        else:
            print(' {} X {} = {}'.format(i,j,i*j))
