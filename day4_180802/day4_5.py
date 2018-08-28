# 파일 읽기
# 파일변수 = open('파일경로', 'r')
f = open('data/yesterday.txt','r')

# 리스트로 변경하기
# 리스트이름 = 파일변수.read() = f.read()

data = f.read()
print(data)
print(type(data)) # String
print(data[0]) # Y
print(data[0:9])
myList = data.split()
print(myList, type(myList))
print(' 단어별로 출력 :')

for i in myList:
    print(i)
    # 단어의 갯수는 몇개일까요?
    print('단어 갯수 :',len(myList))
f.close()

# 퀴즈 : 
# 파일을 읽은 후 단어의 갯수를 출력하는 함수.
'''
fileread('data/Yesterday.txt')

단어 갯수 : 134
'''
print('-'*30)
fileread = open('data/Yesterday.txt','r')
a = fileread.read()
myList = a.split()
print('단어 갯수 : ',len(myList))

print('-'*30)
b = open('data/애국가.txt','r')
Korea = b.read()
print(Korea)
words = Korea.split()
print(words)
print('단어갯수 : ',len(words))

# 파일 읽기
# 파일변수 = open('파일경로', 'r')
# 첫번째 줄만 출력하기 -> 문자열
# 변수 = 파일변수.readline()
f = open('data/애국가.txt','r')
data2 = f.readline()
print(data2, type(data2))
# Yesterday
# <class 'str'>
f.close()

# 파일 읽기
# 파일변수 = open('파일경로', 'r')
# 한줄씩 읽어서 리스트 요소로 저장
# 리스트이름 = 파일변수.readlines()
f = open('data/애국가.txt','r')
data3 = f.readlines()
print(data3, type(data3))
# 리스트 요소 단위로 출력하기
for i in data3:
    print(i)

f.close()
# 퀴즈
'''
  샘플 텍스트 파일의 줄수가 몇개인지 출력하여라.
'''
f = open('data/애국가.txt','r')
data4 = f.readlines()
print('샘플 텍스트 파일의 줄 수는 :',len(data4))

# 퀴즈
'''
data/data.txt

파일의 숫자 모두의 합과 평균을 구한다.
'''
def sumAvr(fileurl):
    f = open(fileurl,'r')
    data = f.readlines()
    total = 0
    for line in data:
        score = int(line)
        total += score
        # 평균 구하기
        avr = total/len(data)

    print('데이터 수 = ',len(data))
    print(' 합 = ', total)
    print(' 평균 = ', avr)
    f.close()

sumAvr('data/data.txt')

def sumWord(fileUrl):
    f = open(fileUrl,'r')
    data = f.read()
   # 공백 없애기
   #data = data.replace(' ','')
   # 개행 없애기
    data = data.replace('\n','')
    print('글자 수 =', len(data))
    f.close()

sumWord('data/data2.txt')






