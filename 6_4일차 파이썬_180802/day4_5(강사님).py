# 파일 읽기 
# 파일변수 = open('파일경로', 'r')
f = open('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt','r')

# 문자열로 변경하기 
# 문자열변수 = 파일변수.read()

data = f.read()
print(data)
print(type(data))  # String
print(data[0]) # Y 첫글자 
print(data[0:10])
myList = data.split()
print(myList, type(myList))
print('단어별로 출력 :')
for i in myList:
    print(i)
# 단어의 갯수는 몇개일까요?    
print( '단어 갯수 : ',len(myList) )
f.close()

# 퀴즈 : 
# 파일을 읽은 후 단어의 갯수를 출력하는 함수 
'''
fileread('data/Yesterday.txt')

단어 갯수 :  134
'''
def fileread(fileUrl):
    f = open(fileUrl,'r') 
    data = f.read()
    myList = data.split()
    print('*'*30)
    print('파일명 : ', fileUrl)
    print(data)
    print( '단어 갯수 : ',len(myList) )
    f.close()   

fileread('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt')


# 파일 읽기 
# 파일변수 = open('파일경로', 'r')
# 첫번째 줄만 출력하기 -> 문자열
# 문자열변수 = 파일변수.readline()
f = open('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt','r')
data2 = f.readline()
print(data2, type(data2))   
# Yesterday
# <class 'str'>
f.close()

# 파일 읽기 
# 파일변수 = open('파일경로', 'r')
# 한줄씩 읽어서 리스트 요소로 저장 
# 리스트이름 = 파일변수.readlines()
f = open('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt','r')
data3 = f.readlines()
print(data3, type(data3))  
# 리스트 요소 단위로 출력하기 
for i in data3:
    print(i,end='')
f.close()
# 퀴즈 
'''
  샘플텍스트파일의 줄수가 몇개인지 출력하여라
'''

print( '\n\n 퀴즈 : 파일의 행수는 몇개일까요?')
def lineRead(fileUrl):
    f = open(fileUrl,'r') 
    data = f.readlines()
    print('*'*30)
    print('파일명 : ', fileUrl)
    print(data)
    print( '행 수 : ',len(data) )
    f.close() 

lineRead('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt.txt')
lineRead('C:\\Users\\HOJIN\\Desktop\\Python\\data\\Yesterday.txt.txt')

# 퀴즈 
'''
data/data.txt

파일의 숫자 모두의 합과 평균을 구한다. 
'''
def sumAvr(fileUrl):
    f = open(fileUrl,'r') 
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

sumAvr('C:\\Users\\HOJIN\\Desktop\\Python\\data\\data.txt')    


def sumWord(fileUrl):
    f = open(fileUrl,'r') 
    data = f.read()
    # 공백 없애기 
    data = data.replace(' ','')
    # 개행 없애기 
    data = data.replace('\n','')
    print(data)
    print('글자 수 = ', len(data))    
    f.close() 

sumWord('data/data2.txt')    