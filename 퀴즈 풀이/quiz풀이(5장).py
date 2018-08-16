
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

# 풀이
with open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\Hojin.txt','w') as f:
    for n1 in range(1,10):
        for n2 in range(1,10):
            f.write('{} X {} = {} \n '.format(n1,n2,n1*n2))

# 풀이2
with open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\gugu1.txt','w') as f:
    f.write('Result ----\n')
result = []
for n1 in range(1,10):
    for n2 in range(1,10):
        data = str(n1) + 'X' + str(n2) + ' = ' + str(n1*n2) + str('\n')
        result.append(data)
with open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\gugu1.txt','a') as f:
    for line in result:
        f.write(line)

