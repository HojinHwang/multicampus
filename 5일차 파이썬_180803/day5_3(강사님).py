# 클래스 생성 
#  def __init__(self, 인자) -> 생성자 함수 (속성정의)
#  def 메소드이름(self, 인자):
#       명령문
#       return value

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
        print('먹는다')   
    # 인자가 있는 메소드 
    def info(self,name,gender,age,job):
        print('이름은 {}, 성별은 {}, 나이는 {}, 직업은{}'.format(name,gender,age,job))             
    # 리턴값이 있는 메소드 
    def age_return(self,age):
        print('나이 + 100 = ')
        return age+100


# 클래스 인스턴스화 
p1 = Person('Robert','man',20,'student')
print('\n'*10,'인스턴스 속성 출력 ')
print('이름은 {}, 성별은 {}, 나이는 {}, 직업은{}' \
.format(p1.name,p1.gender,p1.age,p1.job))

# 정의된 메소드 호출하기 
# 인스턴스이름.메소드(인자)
p1.walk()
p1.eat()
p1.info('Robert','man',20,'student')
print(p1.age_return(20))

# 사각형 클래스 생성 후 
# 사각형의 속성을 출력하는 메소드정의
# 사각형의 넓이 값을 리턴하는 메소드 정의 
'''
사각형의 넓이는 10
사각형의 높이는 20
사각형 면적 :  200
'''
class Square:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def info(self,width,height):
        print('사각형의 넓이는',width)    
        print('사각형의 높이는',height)    
    def area(self,width,height):
        areaValue = width*height
        return areaValue      

s = Square(10,20)
s.info(10,20)
print('사각형 면적 : ',s.area(10,20))

# 퀴즈 1
'''
타원을 클래스 생성, 반지름 속성, 
메소드 정의 - 지름계산, 면적계산
인스턴스화 시킨 후 다음과 같이 출력한다 
 [ 출력형태 : ]
원의 반지름 : ?
원의 지름 : ?
원의 면적 :  ?
'''

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def info(self,radius):
        print('원의 반지름 : ',radius)    
    def diameter(self,radius):
        print('원의 지름 : ',radius*2)         
    def area(self,radius):
        print('원의 면적 : ',3.14*radius**2)         

c = Circle(10)
c.info(10)
c.diameter(10)
c.area(10)



# 퀴즈 2
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
# class Calculator:
#     def __init__(self,n1,n2):
#         self.n1 = n1
#         self.n2 = n2
#     def info(self,n1,n2):
#         print('첫번째 숫자 : ', n1)    
#         print('두번째 숫자 : ', n2)    
#     def c_method1(self,n1,n2):
#         print('더하기 : ', n1+n2)               

# c = Calculator(10,20)
# c.info()
# c.c_method1(10,20)


# 상속이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다. 
# class 클래스이름(부모클래스1,부모클래스2...)

# 부모 클래스 정의 
class phone:
    # 속성 정의 
    def __init__(self,kind):
        self.kind = kind
    def info(self,kind):
        print(' 종류 : ',kind)

class Internet:
    def __init__(self,wifi):
        self.wifi = wifi
    def print_wifi(self):
        print('와이파이 무제한')    
    

# 부모 클래스를 상속받는 자식 클래스 정의 
class mobile(phone, Internet):
    def __init__(self,kind,wifi,color):
        self.kind = kind
        self.wifi = wifi
        self.color = color
    def show(self):
        print(' Pass ')

# 자식 클래스 인스턴스화 
m = mobile('모바일','sk','red')
print(m.kind)
print(m.wifi)
print(m.color)

m.info('스마트폰') # phone  메소드 
m.print_wifi()     # Internet 메소드 
m.show()  # mobile 추가로 정의한 메소드 

# 퀴즈 
'''
  부모 클래스를 2개 이상 정의 한 후 
  자식 클래스가 상속받게 한다. 
  
  부모클래스1 - 아파트, 차 
  부모클래스2 - 오피스텔, 전동스쿠터 
  자식클래스3 - 아파트, 차 , 오피스텔, 전동스쿠터

'''
class Papa:
    # 속성 정의 
    def __init__(self):
        pass
    def info1(self):
        return '아파트, 차 '
class Mama:
    # 속성 정의 
    def __init__(self):
        pass
    def info2(self):
        return '오피스텔, 전동스쿠터 '
class Me(Papa, Mama):
    pass
m = Me()
print(' 상속 : ', m.info1(), m.info2())


print('\n'*10)