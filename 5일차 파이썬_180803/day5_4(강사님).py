# 함수의 종류 
# - 내장함수 
#   : import 명령없이 사용할 수 있는 함수 
#     len(리스트,문자열...)
#     type(변수, 값, 리스트, 클래스...) 
#   : import 명령을 실행해야만 사용할수 
#      있는 함수 
#      
# - 사용자정의함수 
#    def 명령으로 정의하는 함수 


# abs(숫자) : 절대값 추출
print('-10 : ', abs(-10))

# divmod(숫자1,숫자2) : 숫자1/숫자2 
#   : 몫과 나머지 값을 튜플구조로 출력

result = divmod(10,5)
print(result, type(result))
# (2, 0) <class 'tuple'>
print('몫 : {}, 나머지 : {}'\
.format(result[0],result[1]))


# eval(data) 
# - data를 계산식으로 변경해서 결과값 출력 

# data = input('계산식을 입력하세요.. 예) 3+4    ')
# print(data)
# result = eval(data)
# print(data,' = ', result)


# max(data(리스트,튜플...))
# 데이타중에서 최대값 출력 
# min(data(리스트,튜플...))
# 데이타중에서 최소값 출력 

print('최대값구하기 ', max([34,50,100,1,20]))
print('최소값구하기 ', min([34,50,100,1,20]))

# enumerate(데이타(리스트,튜플),인덱스시작번호 )
# 데이타의 색인 생성 
# 리스트 구조로 변경
# list(enumerate(데이타(리스트,튜플),인덱스시작번호 ))

my_list = ['바나나','사과','수박','포도']
for i, v in enumerate(my_list,1):
    print(v, i)

result = list(enumerate(my_list,1))
print(result)
# [(1, '바나나'), (2, '사과'), (3, '수박'), (4, '포도')]
print(result[0])


# map(정의된함수,데이타(리스트,튜플)) -> map오브젝트 생성
# list(map(정의된함수,데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다. 
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
# 문자열안에 숫자가 아닌 글자가 들어가면 True
# 문자열변수.isalpha()
# isdigit()
# 문자열안에 숫자만으로 되어있으면 True
# 문자열변수.isdigit()
str1 = '가나다' # 문자 
str2 = '1234' # 숫자문자 
print(str1.isalpha()) 
print(str1.isdigit()) 
print(str2.isalpha())
print(str2.isdigit())

# filter(함수명,데이타(리스트)) -> 필터 객체 
# list(filter(함수명,데이타(리스트))) -> 리스트 
# 리스트 요소 중에서 함수 조건에 맞는 것만 필터링 

# 짝수값만 출력 
def judge_fn(value):
    return value % 2 == 0 
print(filter(judge_fn,[1,2,3,4,5]))
print(list(filter(judge_fn,[1,2,3,4,5])))
# <filter object at 0x01271B10>
# [2, 4]

# list(zip(리스트1,리스트2))
# 2개의 리스트 요소를 짝을 지어 출력시킨다. 
# 같은 인덱스 값으로 짝짓는다.  
actor = ['정우성','서우','윤하']
gender = ['남','여','여']

for i, j in zip(actor, gender):
    print(i, j)
print(zip(actor, gender)) 
#<zip object at 0x010A7FA8>   
print(list(zip(actor, gender))) 
# 리스트안에 튜플 스타일로저장 
actor_gender = list(zip(actor, gender))
print(actor_gender[0])

# 퀴즈1 
'''
aList = [78,90,80,50]
bList = [8,100,34,60]
두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
'''
print('\n\n 퀴즈1')
aList = [78,90,80,50]
bList = [8,100,34,60]
a_b_list = aList + bList
print('최소값 : ', min(a_b_list))
print('최대값 : ', max(a_b_list))


# 퀴즈 2
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
print('\n\n\ 퀴즈2')

result_list = []
while True:
    # while 문의 탈출 조건 
    if len(result_list) == 5:
        break
    # 데이터 입력
    data = input('>>> 입력 ? ')
    # 데이터가 숫자인가?
    if data.isdigit():
        result_list.append(data)
        print('데이터 입력되었습니다')    
    else:
        print('숫자가 아닙니다. 다시입력해주세요')
    
print(' 입력된 리스트 = ', result_list)        
