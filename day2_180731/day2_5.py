# 2차원 리스트 정의 1
myList = [0,[1,2,3],10]
print(myList)
# 2차원 리스트 인덱싱
print(myList[0]) # 0
print(myList[1]) # [1,2,3]
print(myList[2]) # 10
print(myList[1][0]) # 1
print(myList[1][1]) # 2
print(myList[1][2]) # 3

# 2차원 리스트 정의 2
# 1차원 리스트로 구성 -> 2차원으로 조합
userName = ['홍길동','춘향이','심청이']
userAge = [20,17,16]
userGender = ['남','여','여']
print(userName,userAge,userGender)
# 3행 3열의 2차원 리스트 구조
userList = [userName,userAge,userGender]
print(userList)
# 춘향이 출력
# 16 출력
# 남 출력
print(userName[1])
print(userAge[2])
print(userGender[0])

# 퀴즈
# [1,3,5,4,2]라는 리스트를 [5,4,3,2,1]로 만들어보자.
'''
a = [1,3,5,4,2]
'''
a = [1,3,5,4,2]
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# ['Life','is','too','short']라는 리스트를 Life too short라는
# 문자열로 만들어 출력해보자
'''
a = ['Life', 'is', 'too' , 'short']
'''
a = ['Life', 'is', 'too' , 'short']
print(a)
print(str(a))
a1 = ' '.join(a)
print(a1 , type(a1))

# 퀴즈
'''
아래의 리스트를 이용하여
grade 2차원 리스트를 만들고
총점과 평균을 과목별로 출력한다.

kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]

grade = [[ 55, 66, 34, 60],[ 78, 90, 45, 88],
[56, 98, 78, 90]]

kor = 총점(), 평균()
math = 총점(), 평균()
eng = 총점(), 평균()
'''

kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]

print(kor,math,eng)
all = [kor,math,eng]
print(all)

K = kor[0]+kor[1]+kor[2]+kor[3]
M = math[0]+math[1]+math[2]+math[3]
E = eng[0]+eng[1]+eng[2]+eng[3]
print(K)
print(M)
print(E)
K1 = K/4
M1 = M/4
E1 = E/4
print(K1)
print(M1)
print(E1)

print('kor 의 총점은 {}이고 {}이다'.format(K,K1))
print('math 의 총점은 {}이고 {}이다'.format(M,M1))
print('eng 의 총점은 {}이고 {}이다'.format(E,E1))




