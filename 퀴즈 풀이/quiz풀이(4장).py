# 퀴즈 : 
# 파일을 읽은 후 단어의 갯수를 출력하는 함수 
'''
fileread('data/Yesterday.txt')

단어 갯수 :  134
'''

# 첫번째 풀이
f = open('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt','r')
data = f.read()
myList = data.split()
print('단어갯수 : ',len(myList))
f.close()

# 두번째 풀이
def fileread(fileUrl):
    f = open(fileUrl,'r')
    data = f.read()
    myList = data.split()
    print('단어갯수 : ',len(myList))
    f.close()
fileread('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt')

# 퀴즈 
'''
  샘플텍스트파일의 줄수가 몇개인지 출력하여라
'''
def textfile(fileUrl):
    f = open(fileUrl,'r')
    data = f.readlines()
    print('줄 수 :', len(data))
    f.close()
textfile('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt')

# 퀴즈
'''
data/data.txt

파일의 숫자 모두의 합과 평균을 구한다. 
'''
# 풀이

def sumAvr(fileUrl):
    f = open(fileUrl,'r')
    data = f.readlines()
    sum = 0
    for line in data:
        score = int(line)
        sum += score
    Avr = sum/len(line) # line이 세로로 값이 나옴 즉 각 줄의 갯수를 나타냄.
    print('파일의 숫자 모두의 합 : ', sum)
    print('파일의 숫자 모두의 평균 : ', Avr)
    f.close()
sumAvr('C:\\Users\\HOJIN\\Desktop\\Python\\data\\data.txt')

def sumWord(fileUrl):
    f = open(fileUrl,'r') 
    data = f.read()
    # 공백 없애기 
    data = data.replace(' ','') # replace ('기존','바꿀것')
    # 개행 없애기 
    data = data.replace('\n','')
    print(data)
    print('글자 수 = ', len(data))    
    f.close() 

sumWord('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\data2.txt')

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
# 풀이
myList = ['바나나','쥬라기 공원', '장미','파이썬','원숭이']
f = open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\myList.txt','w')
f.write('Result ---- \n\n')
for i in myList:
    print(i)
    data = i + '\n'
    f.write(data)
f.close()

# 퀴즈
# data.txt 안에 숫자를 이용하여 
# 합과 평균을 구한다. 
# 그결과를 result.txt에 출력한다. 

# 풀이 1
def calculator(fileUrl):
    f = open(fileUrl,'r')
    data = f.readlines()
    sum = 0
    for line in data:
        score = int(line)
        sum += score
        avr = sum/len(data)
    print('합 : ',sum)
    print('평균 : ',avr)
    f.close()
calculator('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\data.txt')

f = open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\result.txt','w')
f.write('Result ---- \n\n')
f.write('합 : 629')
f.write('\n평균 : 78.625')
f.close()

f = open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\data.txt','r')
data = f.readlines()
total = 0
for line in data:
    score = int(line)
    total += score
    avr = total/len(data)
print('수들의 길이 : ', len(data))
print('수들의 합 : ', total)
print('수들의 평균 : ', avr)
f.close()
f = open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\result2.txt','w')
f.write('Result ---- \n\n')
data1 = '수들의 합 : ' + str(total) + '\n'
data2 = '수들의 평균 : ' + str(avr)
f.write(data1)
f.write(data2)
f.close()
