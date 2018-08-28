
# 파일 읽기 
# 파일변수 = open('파일경로', 'r')
#  예) f = open('data/Yesterday.txt','r')

# 파일에 관련된 함수 - 파일변수.함수(옵션)
# 파일변수.read() -> 문자열 
# 파일변수.readline() -> 문자열 
# 파일변수.readlines() -> 리스트 
# 파일변수.write()

# 파일변수.write(데이타)

# with 문 - 별도의 close() 를 사용하지 않아도 된다. 
# with 문안에 들여쓰기 주의 
# with open(파일경로, 모드(r,w,a), [인코딩] ) as 파일변수:
#   명령문 

'''
f = open('data/Yesterday.txt','r')
data = f.read()
print(data)
f.close()
'''
# with 문으로 파일을 읽고 출력하기 
with open('data/Yesterday.txt','r') as f:
    data = f.read()
    print(data)

# with 문으로 파일을 읽고 한줄만 출력하기 
print('-'*30)
with open('data/test.txt','r') as f:
    data = f.readline()
    print(data)


# with 문으로 파일을 읽고 리스트로 변환하여 출력하기 
print('-'*30)
with open('data/test.txt','r') as f:
    data_list = f.readlines()
    print(data_list, type(data_list))
    # 리스트 출력하기 
    cnt = 1
    for line in data_list:
        print(cnt,'번째 라인',line, end='')
        cnt += 1

# with 문으로 빈파일 만들기 
'''
f=open('data/result_0803.txt','w')
f.close()
'''
print('-'*30)
with open('data/result_0803.txt','w') as f:
    pass

# with 문으로 파일 생성후 문자열과 리스트 저장하기 
print('-'*30)
fruits = ['바나나 \n','사과 \n','포도 \n']
with open('data/result_0803.txt','w') as f:
    f.write('오늘은 금요일 ....\n 내일은 토요일')
    msg = '\n\n 모레는 일요일'  
    f.write(msg)  
    # 리스트 출력하기 
    for line in fruits:
        f.write(line)

# 외부 텍스트 파일을 읽어서 새로운 파일에 저장하기 
# 파일 복사 
print('-'*30)
# 데이타 읽기 
with open('data/Yesterday.txt','r') as f:
    data = f.read()  # 문자열 

# 데이타 쓰기 
print('-'*30)
with open('data/result_ys.txt','w') as f:
    f.write(data)

# 퀴즈 
'''
Yesterday.txt 파일에서 1번째줄만 result.txt 파일에 
저장하여라
'''
print('-'*30)
# 데이타 읽기 
with open('data/Yesterday.txt','r') as f:
    data = f.readline()  # 문자열
    print(data)
# 데이타 쓰기 
with open('data/result.txt','w') as f:
    f.write(data)


# 데이타 읽기 
with open('data/Yesterday.txt','r') as f:
    data = f.readlines()  # 리스트
    print('첫번째 리스트 출력 : ',data[0])
# 데이타 쓰기 
with open('data/result.txt','w') as f:
    f.write(data[0])

# 기존 파일에 내용 추가하기 
# open(파일경로,'a') - append
with open('data/result.txt','a') as f:
    f.write(' \n\n 새로운 내용 추가 ')

f2= open('data/result.txt','a')  
f2.write(' \n\n 새로운 내용 추가 ')
f2.close()

# 퀴즈 
'''
    구구단을 gugu.txt에 결과를 출력한다. 

f.wirte(텍스트이어야함,문자열변수, 문자열, 
리스트요소(list[0]))

1) 빈 리스트 생성 - result = []
2) 구구단 출력 값 -> 리스트 
  - 데이타 값이 정수 -> str(데이터) -> 문자열
    result.append()
   
3) 파일 출력하기 
   파일 생성 후 
    for i in result:
        f.write(i)
'''





# 파일 생성 
with open('data/gugu.txt', 'w') as f:
    f.write('\n\n 파일이 생성되었습니다. \n\n ')

# 빈리스트 생성 
result = []

# 구구단 
for i in range(2,10):
    for j in range(1,10):
        # 리스트 요소 생성 
        data = str(i) +' x '+ str(j)+' = ' + str(i*j)+str('\n')
        # 리스트 추가 
        result.append(data)
        # 화면 찍기 
        print('{} X {} = {}'.format(i,j,i*j))

# 전체 리스트 찍기 
print('result = ', result)

# 파일에 저장 
with open('data/gugu.txt', 'a') as f:
    for line in result:
        f.write(line)
    print('파일 출력 완료')
