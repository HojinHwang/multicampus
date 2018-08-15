
# 파일 읽기 
# 파일변수 = open('파일경로', 'r')
# 예 ) f = open('data/Yesterday.txt','r')

# 파일에 관련된 함수 - 파일변수.함수()
# 파일변수.read() -> 문자열
# 파일변수.readline() -> 문자열
# 파일변수.readlines() -> 리스트
# 파일변수.write()

# 파일변수.write(데이터)

# with 문 - 별도의 close()를 사용하지 않아도 된다.
# with 문안에 들여쓰기 주의
# with open(파일경로, 모드(r,w,a), [인코딩]) as 파일변수:
#   명령문 


'''
f = open('data/Yesterday.txt'.'r')
data = f.read()
print(data)
f.close()
'''
# with 문으로 파일을 읽고 출력하기
with open('data/Yesterday.txt','r') as f:
    data = f.read()
    print(data)

# with 문으로 파일을 읽고 한줄만 출력하기
print('*'*30)
with open('data/애국가.txt','r') as f:
    data = f.readline()
    print(data)

# with 문으로 파일을 읽고 리스트로 변환하여 출력하기
print('*'*30)
with open('data/애국가.txt','r') as f:
    data_list = f.readlines()
    print(data_list,type(data_list))
    # 리스트 출력하기
    cnt = 1
    for line in data_list:
        print(cnt,'번째 라인',line, end='')
        cnt += 1

# with 문으로 파일 쓰기
'''
f = open('data/result_0803.txt/'w')
f.close()
'''

# with 문으로 파일 생성후 문자열과 리스트 저장하기
print('-'*30)
with open('data/result_0803.txt','w') as f:
    f.write('오늘은 금요일 .....\n쉬는시간 신이만든시간')
    msg = '\n\n쉬는시간 신이만든시간'
    f.write(msg)

# wiht 문으로 파일 생성후 문자열과 리스트 저장하기
print('-'*30)
fruits = ['바나나','사과','포도']
with open('data/result_0803.txt','w') as f:
    f.write('오늘은 금요일 .....\n쉬는시간 신이만든시간')
    msg = '\n\n쉬는시간 신이만든시간'
    f.write(msg)
    # 리스트 출력하기
    for line in fruits:
        f.write(line)

# 외부 텍스트 파일을 읽어서 새로운 파일에 저장하기
print('-'*30)
# 데이터 읽기
with open('data/Yesterday.txt','r') as f:
    data = f.read() # 문자열

# 데이터 쓰기
print('-'*30)
with open('data/result_ys.txt','w') as f:
    f.write(data)

# 퀴즈
'''
Yesterday.txt 파일에서 1번째줄만 result.txt 파일에 저장하여라
'''

with open('data/Yesterday.txt','r') as f:
    data = f.readline()
    print(data)


# 기존 파일에 내용 추가
# open(파일경로,'a') - append
with open('data/애국가.txt','a') as f:
    f.write(' \n\n새로운 내용 추가 ')

f2 = open('data/애국가.txt','a')
f2.write(' \n\n새로운 내용 추가 ')
f2.close()


# 퀴즈
'''
구구단을 gugu.txt에 결과를 출력한다.

f.write(텍스트 이여야 함 문자열변수, 문자열, 리스트요소(list[0]))

1) 빈 리스트 생성 - result = []
2) 구구단 출력 값 -> 리스트
   result.append()
구구단 출력
  - 데이터 값이 정수 -> str(데이터) -> 문자열
3) 파일 출력하기
   파일 생성 후
   for i in result
      f.write(i)
'''



with open('data/gugu.txt','w') as f:
    for i in range(1,10):
        for j in range(1,10):
            f.write(' \n\n{} X {} = {}'.format(i,j,i*j))



