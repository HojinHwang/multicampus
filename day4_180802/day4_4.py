# 가변인자 *인자명
# def 함수명 (*인자):
#   명령문
#   return
# 인자 여러개 있는것을 가변인자라고 함.
def print_n(*value):
    for i in value:
        print(i)

print_n('Python')
print_n('Victory','Sunday')
print_n(100,200,500)

def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
        return sum


# 전역변수 선언
# 함수안에 global 변수
# 함수 블록 밖에서도 같은 변수일때 영향을 끼친다.

a = 5
print(a)
def test():
    global a
    a = 10
    print(a)


# 람다함수 : 익명함수
# 임시적인 함수
# 함수변수 = lambda 인자 : 명령문
# 함수 호출시
# 함수변수(인자)

f = lambda x, y: x+y
print(f(12,20))

g = lambda x : x**2
print(g(12))
