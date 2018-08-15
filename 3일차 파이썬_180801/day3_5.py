# 시간과 관련된 모듈 임포트
import datetime

# 시간 전체에 관련된 변수 설정
# 현재 년도, 월, 시간
now = datetime.datetime.now()

print('now = ',now)
# 현재 년도만 추출
print(' 년도 =',now.year)
print(' 월 =',now.month)
print(' 일 =',now.day)
print(' ? =',now.date)
print(' 시간 =',now.hour)

# 퀴즈 :
# 오늘은 2018년 8월 1일 입니다.
# 현재시간은 ()시 ()분입니다.

import datetime
today = datetime.datetime.today()
print('오늘은 {}년 {}월 {}일 입니다.'.format(today.year,
today.month,today.day))
print('현재시간은 {}시{}분입니다.'.format(today.hour,today.minute))

print(type(now.hour)) # class 'int'

# 퀴즈1 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 출력한다.
# 현재 시간은 오후 (3)시 ()분입니다.

import datetime
today = datetime.datetime.today()
if today.hour ==3:
    print('현재시간은 오후 {}시{}분입니다.'.format(today.hour,today.minute))

# 퀴즈2 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을, 겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 8월은 여름입니다.

import datetime
now = datetime.datetime.now()
if 3 <= now.month <= 5:
    print('{}월은 봄입니다!'.format(now.month))
elif 6 <= now.month <= 8:
    print('{}월은 여름입니다!'.format(now.month))
elif 9 <= now.month <= 11:
    print('{}월은 가을입니다!'.format(now.month))
else:
    print('{}월은 겨울입니다!'.format(now.month))


# 요일 찍기
# 요일은 0(월요일)) ~ 6(일요일)
today = datetime.datetime.today().weekday()
print(today) # 2
if today == 2:
    print('수요일 입니다.')


# 퀴즈 :
# 아래와 같이 출력해보세요
# 2018년 8월 1일 수요일

# 방법
# 요일 리스트를 정의한 후 요일 인덱스를 리스트 인덱스로 활용
import datetime
now = datetime.datetime.now()
t = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
today = datetime.datetime.today().weekday()
print(t[today])
print('{}년 {}월 {}일 {}'.
format(now.year,now.month,now.day,t[today]))

