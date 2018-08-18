# 클래스 생성
#   def __init__(self,인자) -> 생성자 함수 (속성정의)
#   def 메소드이름(self, 인자):
#       명령문

# 사람 클래스
class Person:
    # 속성정의를 위한 생성자 함수
    def __init__(self,name,gender,age,job):
        self.name = name
        self.gender = gender
        self.age = age
        self.job = job
    # 메소드 정의
    def walk(self):
        print('걷는다.')
    def eat(self):
        print('먹는다.')
    def info(self,name,gender,age,job):
        print('이름은 {}, 성별은{}, 나이는{}, 직업은 {}'.format(name,gender,age,job))
# 리턴값이 있는 메소드
    def age_return(self,age):
        return age+100

# 클래스 인스턴스화
p1 = Person('Hojin','Man',23,'college')
p2 = Person('Boseok','Man',23,'gongik')
print('이름은 {}, 성별은 {}, 나이는 {}, 직업은 {}'.format(p1.name,p1.gender,p1.age,p1.job))

# 정의된 메소드 호출하기
# 인스턴스이름.메소드(인자)
p1.walk()
p1.eat()
p1.info('Hojin','man',23,'college')
print(p1.age_return(20))

# 사각형 클래스 생성후 사각형의 속성을 출력하는 메소드정의
# 사각형의 넓이 값을 리턴하는 메소드 정의
class square:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def info(self,width,height):
        print('사각형의 넓이는',width)
        print('사각형의 길이는',height)
    def area(self,width,height):
        areaValue = width*height
        return areaValue

s = square(10,20)
s.info(10,20)
print('사각형 면적: ',s.area(10,20))

# 퀴즈
'''
타원을 클래스로 생성, 반지름 속성,
메소드 정의 - 지름계산, 면적계산
인스턴스화 시킨 후 다음과 같이 출력한다.

출력형태 :

원의 반지름 : ?
원의 지름 : ?
원의 면적 : ?

'''

class ellipse:
    def __init__(self,radius):
        self.radius = radius
    def info(self,radius):
        print(' 지름은 ',2*radius)
        print(' 면적은 ',radius**2*3.14)

r = ellipse(10)
r.info(10)

# 퀴즈 2
'''
2개의 숫자를 속성으로 가진 계산기 클래스 만들기


인스턴스화 시킨 후 다음과 같이 출력한다
[ 출력형태 : ]
첫번쨰 숫자 : ?
두번쨰 숫자 : ?
더하기 : ?
빼기 : ?
곱하기 : ?
나누기 : ?
'''

class caculator:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def info(self,n1,n2):
        print('첫번째 숫자 :',n1)
        print('두번째 숫자 :',n2)
    def sum(self,n1,n2):
        print('{} + {} : {}'.format(n1,n2,n1+n2))




# 상속이란 ?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1, 부모클래스2 ...)


# 부모 클래스 정의
class phone():
    # 속성 정의
    def __init__(self,kind):
        self.kind = kind
    def info(self,kind):
        print(' 종류 : ',)

class Internet:
    def __init__(self,wifi):
        self.wifi = wifi
    def print_wifi(self):
        print('와이파이 무제한')



# 부모 클래스를 상속받는 자식 클래스
class mobile(phone, Internet):
    def __init__(self,kind,wifi,color):
        self.kind = kind
        self.wifi = wifi
        self.color = color
    def show(self):
        print(' Pass ')

# 자식 클래스 인스턴스화
m = mobile('모바일','sk','검은색')
print(m.kind)
print(m.wifi)
print(m.color)

m.info('스마트폰') # phone 메소드
m.print_wifi()      # Internet 메소드
m.show()    # mobile 추가로 정의한 메소드

# 퀴즈
'''
    부모 클래스를 2개이상 정의한 후
    자식 클래스가 상속받게 한다.

    부모클래스1 - 아파트, 차
    부모클래스2 - 오피스텔, 전동스쿠터
    자식클래스3 - 아파트, 차, 오피스텔, 전동스쿠터
'''

class money():
    def __init__(self,apart,car):
        self.apart = apart
        self.car = car
    def info1(self,apart,car):
        print(' 부모클래스 1 : ',apart,car)

class money1():
    def __init__(self,opistel,scooter):
        self.opistel = opistel
        self.scooter = scooter
    def info2(self,opistel,scooter):
        print(' 부모클래스 2 :',opistel,scooter)

class child(money,money1):
    def __init__(self,apart,car,opistel,scooter):
        self.apart = apart
        self.car = car
        self.opistel = opistel
        self.scooter = scooter

me = child('아파트','자동차','오피스텔','스쿠터')
print(me.info1('아파트','자동차'))
print(me.info2('오피스텔','스쿠터'))










