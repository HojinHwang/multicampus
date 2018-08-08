# 파일생성 
# 파일변수 = open(파일경로및파일명,'w')
f = open('data/test2.txt','w')
f.close()

# 파일 생성 후 데이터 입력하기 
# 파일변수 = open(파일경로및파일명,'w')
# 파일변수.write(데이타)

f = open('data/test2.txt','w')
f.write('Result ---- \n\n')
f.write('_'*40)
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# 퀴즈 
'''
myList = ['바나나','쥬라기 공원', 
'장미','파이썬','원숭이']

data\myList.txt 파일 생성 후 
myList에 정의된 리스트 요소를 삽입한 후 
결과 확인 

myList.txt 문서안에는 
바나나
쥬라기 공원
... 

'''
myList = ['바나나','쥬라기 공원', \
'장미','파이썬','원숭이']
print(myList)
f = open('data/myList.txt','w')
f.write('Result ---- \n\n')
for i in myList:
    # f.write(i)
    data = i + '\n'
    f.write(data)
f.close()

# data.txt 안에 숫자를 이용하여 
# 합과 평균을 구한다. 
# 그결과를 result.txt에 출력한다. 
'''
result.txt 결과가 아래와 같이 저장 

데이터 수 =  ?
합 =  ?
평균 =  ?

'''
f = open('data/data.txt','r') 
data = f.readlines() #리스트화 
total = 0
# 합계 구하기 
for line in data:
    score = int(line)
    total += score
# 평균 구하기     
avr = total/len(data)   
print('데이터 수 = ', len(data))        
print('합 = ', total)        
print('평균 = ', avr)        
f.close() 
f = open('data/result.txt','w')
f.write('Result ---- \n\n')
data1 = '합 = ' + str(total)
data2 = '\t 평균 = ' + str(avr)
f.write(data1)
f.write(data2)
# data = '\n\n 데이터 수 = '+ str(len(data)) + \
#         '\n\n 합 = ' + str(total) + \
#         '\n\n 평균 = '+ str(avr)
# f.write(data)
f.close()

# 퀴즈 
'''
2개의 텍스트 파일 Yesterday.txt, test.txt
파일의 데이터를 
result2.txt에 함께 출력한다. 
'''

f1 = open('data/test.txt','r') 
f2 = open('data/Yesterday.txt','r') 
f = open('data/result2.txt','w')
data1 = f1.readlines() #리스트화 
data2 = f2.readlines() #리스트화 
myList = ['*** 1번째 파일\n\n'] + data1 + ['\n\n *** 2번째 파일 \n\n'] + data2

for i in myList:
    # data = '\n' + i
    data = i
    f.write(data)
f1.close()    
f2.close()
f.close()