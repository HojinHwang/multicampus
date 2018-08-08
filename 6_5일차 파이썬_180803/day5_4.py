# 함수의 종류
# - 내장함수
#   :  import 없이 사용할 수 있는 함수
#      len(리스트,문자열...)
#      type(변수, 값, 리스트, 클래스...)
#   : import 명령을 실행해야만 사용할수 있는 함수
#
# - 사용자정의함수
#   def 명령으로 정의하는 함수


# abs(숫자) : 절대값 추출
print(' -10 : ', abs(-10))

# divmod(숫자1,숫자2) : 숫자1/숫자2 몫과 나머지 출력

result = divmod(10,3)
print(result,type(result))
# (3,1) <class 'tuple'>
print('몫 : {}, 나머지 : {}'.format(result[0],result[1]))


# eval(data)
# - data를 계산식으로 변경해서 결과값 출력
data = input('계산식을 입력하시오 .. 예) 3+4  ')
print(data)
result = eval(data)
print(data,' = ', result)


# max(data(리스트,튜플...))
# 데이터중에서 최대값 출력
# min(data(리스트,튜플...))
# 데이터중에서 최소값 출력


print('최대값 구하기 ',max([1,2,5,9,66,99,555]))
print('최소값 구하기 ',min([1,2,5,9,66,99,555]))


# enumerate(데이터(리스트,튜플),인덱스시작번호)
# 데이터의 색인 생성
# enumerate(데이터(리스트,튜플),인덱스시작번호))
my_List = ['apple','banana']
for index, value in enumerate(my_List,1):
    print(index,value)


result = list(enumerate(my_List,1))
print(result)
# [(1, 'apple'), (2, 'banana')]
print(result[0])


# map(정의된함수,데이터(리스트,튜플)) -> map오브젝트 생성
# list(map(정의된함수,데이터(리스트,튜플)))
# 데이터 요소를 정의된함수의 결과값으로 리턴한다.
def power_fn(value):
    return value**2
print(map(power_fn, [1,2,3,4]))
print(list(map(power_fn, [1,2,3,4])))

result = []
for i in [1,2,3,4]:
    data = i**2
    result.append(data)
print(result)


# isalpha()
# 문자열안에 모두 숫자가 아닌 글자가 들어가면 True
# 문자열변수.isalpha()
# isdigit()
# 문자열안에 숫자만으로 되어있으면 True
# 문자열변수.isdigit()
str1 = '가나다' # 문자
str2 = '1234' # 숫자문자
print(str1.isalpha()) # T  
print(str1.isdigit()) # F
print(str2.isalpha()) # F
print(str2.isdigit()) # T


# filter(함수명,데이터(리스트)) -> 필처 객체
# list(filter(함수명,데이터(리스트)))
# 리스트요소 중에서 함수 조건에 맞는 것만 필터링

# 짝수값만 출력

def judge_fn(value):
    return value % 2 == 0 # 짝수만 pass
print(list(filter(judge_fn, [1,2,3,4,5])))

actor = ['정우성','나나']
gender = ['여','여']
# 2개의 리스트 요소를 짝을 지어 출력시킨다.
for i,j in zip(actor,gender):
    print(i,j)
print(zip(actor, gender))
# <zip object at 0x00000000029F3248>
print(list(zip(actor,gender))) # <zip object at 0x00000000029F3248>
# 리스트안에 튜플 스타일로 저장
actor_gender = list(zip(actor,(gender))
print(actor.gender[0])

# 퀴즈 1
'''
aList = [78,90,80,50]
bList = [8,100,34,60]

두개의 리스트 요소중에서 최대값과 최소값을 출력하여라.
'''


# 퀴즈 2
'''
숫자값으로 구성된 리스트 생성하기
리스트 요소는 5개
result_list = []
리스트요소는 입력을 받는다.
입력받은 데이터가 숫자이면 리스트에 추가
그렇지 않으면 메세지 출력
'''
result_list = []
while True:
    # while 문의 탈출 조건
    if len(result_list) == 5:
        break
    # 데이터 입력

data = input('>>> 입력 > ?')
# 데이터가 숫자인가 ?
if data.isdigit():
    result_list.append(data)
    print('데이터 입력되었습니다.')
    else:
        print('숫자가 아닙니다. 다시 입력해 주세요.')

print(' 입력된 리스트 = ',result_list)
