# CSV 파일 입출력
# 엑셀에서 문서 만들기 -> 파일명.csv 로 저장

# csv 모듈 사용
import csv

# 파일변수 = open('파일경로','모드r,w', encoding='utf-8/cp949')

# csv 파일 읽기
f = open('data/test.csv','r',encoding='cp949') # cp949 = 액셀
csv_data = csv.reader(f) # 데이터 변수 = csv.reader(파일변수) 
# print(csv_data)
# <_csv.reader object at 0x00000000002C93798

for line in csv_data:
    print(line)
f.close()

# 한줄씩 리스트 형식으로 출력하기
print('*'*40)
f = open('data/test.csv','r',encoding='cp949') # cp949 = 액셀
csv_data = csv.reader(f)

data_list = []
for line in csv_data:
    data_list.append(line)

print(data_list[0])
f.close()

# with 문으로 변경하기
print('-'*40)
with open('data/test.csv','r',encoding='cp949') as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        print(line)

# csv 파일로 출력하기
# 리스트 -> csv 파일로 출력
# 리스트요소아이템이 한행씩 입력된다.
# csv라인변수 = csv.writer(파일변수)
# csv라인변수.writerow(데이터)
f = open('data/output.csv','w',encoding='cp949')
wr = csv.writer(f)
wr.writerow([1, 'mkblog'])
wr.writerow([2, 'co'])
wr.writerow([3, 'kr'])
f.close()

# for문을 이용하여 리스트에 정의된 아이템을 csv파일로 저장하기
# 2차원 리스트
fruitsList = [[1,'사과','배'],[2,'토마토','방울토마토'], \
[3,'바나나','귤']]
f = open('data/output_f.csv','w',encoding='cp949', newline='')
wr = csv.writer(f)
for line in fruitsList:
    wr.writerow(line)
f.close

print('*'*40)
with open('data/output_p.csv','w',encoding='cp949') as f:
    pc = csv.writer(f)
    pc.writerow([1, '삼성'])
    pc.writerow([2, '한성'])
    pc.writerow([3, 'LG'])
    print('작업 끝')

# 퀴즈
'''
population.csv 파일 데이터에서 5개만 출력하기
'''
with open('data/population.csv','r',encoding='cp949') as f:
    csv_data = csv.reader(f)
    cnt = 0
    for line in csv_data:
        if cnt == 5:break
        print(line)
        cnt += 1

# 퀴즈
'''
population.csv 파일 읽기
리스트화 시키기
리스트에서 1열만 출력시키기
result_list[?][0]
'''

with open('data/population.csv','r',encoding='cp949') as f:
    csv_data = csv.reader(f)
    # data_list = []
    # for line in csv_data:
    #   data_list.append(line)
    data_list = list(csv_data)
    print('State : ')
    for i in range(1,len(data_list)):
        print(data_list[i][0],',',end='')
print('-'*30)


