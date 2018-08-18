
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
        data = str(n1) + 'X' + str(n2) + ' = ' + str(n1*n2) + str('\n') # 리스트안은 문자열
        result.append(data)
with open('C:\\Users\\HOJIN\\Desktop\\multicampus\\data\\gugu1.txt','a') as f:
    for line in result:
        f.write(line)

# 퀴즈 
# 주변에서 볼 수 있는 사물로 클래스를 선언하고
# 인스턴스화 시켜서 출력한다.

class phone:
    def __init__(self,color,brand,year):
        self.color = color
        self.brand = brand
        self.year = year

phone1 = phone('검은색','애플','2017년')
phone2 = phone('흰색','삼성','2018년')
print('phone1 의 색은 {}, 회사는 {}, 출시년도는 {}' \
.format(phone1.color,phone1.brand,phone1.year))
print('phone2 의 색은 {}, 회사는 {}, 출시년도는 {}' \
.format(phone2.color,phone2.brand,phone2.year))

# 퀴즈
# 사각형 클래스 생성 후 
# 사각형의 속성을 출력하는 메소드정의
# 사각형의 넓이 값을 리턴하는 메소드 정의 
'''
사각형의 넓이는 10
사각형의 높이는 20
사각형 면적 :  200
'''
class square:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def info(self,width):
        print('사각형의 넓이는 :',width)
    def info1(self,height):
        print('사각형의 높이는 :',height)
    def info2(self,width,height):
        print('사각형의 넓이는 :',width*height)
print(' - '*30)
square1 = square(10,20)
square1.info(10)
square1.info1(20)
square1.info2(10,20)

# 퀴즈
'''
타원을 클래스 생성, 반지름 속성, 
메소드 정의 - 지름계산, 면적계산
인스턴스화 시킨 후 다음과 같이 출력한다 
 [ 출력형태 : ]
원의 반지름 : ?
원의 지름 : ?
원의 면적 :  ?
'''
class circle:
    def __init__(self,radius):
        self.radius = radius
    def info(self,radius):
        print('원의 반지름 : ',radius)
    def diameter(self,radius):
        print('원의 지름 : ',radius*2)
    def area(self,radius):
        print('원의 면적 : ',3.14*radius**2)
circle1 = circle(10)
circle1.info(10)
circle1.diameter(10)
circle1.area(10)

# 퀴즈
'''
2개의 숫자를 속성으로 가진 계산기 클래스 만들기 

인스턴스화 시킨 후 다음과 같이 출력한다 
[ 출력형태 : ]
첫번째 숫자 : ?
두번째 숫자 : ?
더하기 : ?
빼기 : ?
곱하기 : ?
나누기 : ?

'''

class calculate:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def info1(self,n1):
        print('첫번째 숫자 : ',n1)
    def info2(self,n2):
        print('두번째 숫자 : ',n2)
    def plus(self,n1,n2):
        print(' 더하기 : ',n1+n2)
    def minus(self,n1,n2):
        print(' 빼기 : ',n1-n2)
    def multiply(self,n1,n2):
        print(' 곱하기 : ',n1*n2)
    def divide(self,n1,n2):
        print(' 나누기 : ',n1/n2)
n1 = int(input('첫번째 숫자 ?'))
n2 = int(input('두번째 숫자 ?'))
C = calculate(n1,n2)
C.info1(n1)
C.info2(n2)
C.plus(n1,n2)
C.minus(n1,n2)
C.multiply(n1,n2)
C.divide(n1,n2)

# 퀴즈 
'''
  부모 클래스를 2개 이상 정의 한 후 
  자식 클래스가 상속받게 한다. 
  
  부모클래스1 - 아파트, 차 
  부모클래스2 - 오피스텔, 전동스쿠터 
  자식클래스3 - 아파트, 차 , 오피스텔, 전동스쿠터

'''
class papa:
    def __init__(self):
        pass
    def info(self):
        return  '아파트','차'
class mama:
    def __init__(self):
        pass
    def info1(self):
        return '오피스텔','전동스쿠터'
class child(papa,mama):
    pass
me = child()
print(' 상속 : ',me.info(),me.info1())

# 퀴즈 
'''
aList = [78,90,80,50]
bList = [8,100,34,60]
두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
'''
aList = [78,90,80,50]
bList = [8,100,34,60]
abList = aList + bList
print(' 최소값 : ',min(abList))
print(' 최대값 : ',max(abList))

# 퀴즈
'''
숫자값으로 구성된 리스트 생성하기 
리스트 요소는 5개로 한정 
1) 빈리스트 생성 
result_list = [] 
2) 

리스트 길이가 5개인가? 
5개라면 리스트 요소 모두 출력 

그렇지 않다면 
  리스트요소 입력 받기 
  입력받은 데이타가 숫자이면 리스트에 추가 
  그렇지 않으면 메세지 출력
  (숫자가 아닙니다. 다시입력해주세요)
... 반복   
'''
result_list = []
while True:
    if len(result_list) == 5:
        break
    data = input(' 리스트요소를 입력해주세요 ')
    if data.isdigit():
        result_list.append(data)
        print('데이터가 입력되었습니다.')
    else:
        print('숫자가 아닙니다. 다시 입력해주세요')

print(' 입력된 리스트 = ',result_list)


