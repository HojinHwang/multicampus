import warnings
warnings.filterwarnings('ignore')

# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install seaborn
import numpy as np
import pandas as pd # csv 파일 읽음
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(
    fname='c:/Windows/Fonts/malgun.ttf').get_name()
    print('font_name=====', font_name)
    rc('font', family=font_name)
else:
    print('Unknown system...')

# tsv : tab seperated value(탭으로 구분된 값)
df = pd.read_csv('data/2016crime.tsv', delimiter='\t',
index_col='자치구')
# print(df.head(10)) 10개 출력

df['살인검거율'] = df['살인(검거)'] / df['살인(발생)'] * 100
df['강도검거율'] = df['강도(검거)'] / df['강도(발생)'] * 100
df['강간강제추행검거율'] = df['강간강제추행(검거)'] / df['강간강제추행(발생)'] * 100
df['절도검거율'] = df['절도(검거)'] / df['절도(발생)'] * 100
df['폭력검거율'] = df['폭력(검거)'] / df['폭력(발생)'] * 100
df['합계검거율'] = df['합계(검거)'] / df['합계(발생)'] * 100
# print(df.head()) # 5개
# df = dataframe

del df['살인(검거)']
del df['강도(검거)']
del df['강간강제추행(검거)']
del df['절도(검거)']
del df['폭력(검거)']
del df['합계(검거)']
print(df.shape) # 전체갯수 알고싶을때 (row, cols) (25, 12)
print(df.head(25))


cols = ['합계검거율','강도검거율','강간강제추행검거율'
,'절도검거율','살인검거율','폭력검거율']

# loc = location
# 100이 넘어가는 값들을 100으로 바꿔라
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['폭력검거율'] > 100, '폭력검거율'] = 100
df.loc[df['절도검거율'] > 100, '절도검거율'] = 100
df.loc[df['강간강제추행검거율'] > 100, '강간강제추행검거율'] = 100
df.loc[df['강도검거율'] > 100, '강도검거율'] = 100
df.loc[df['합계검거율'] > 100, '합계검거율'] = 100

df.rename(columns={'살인(발생)':'살인',
                    '강도(발생)':'강도',
                    '강간강제추행(발생)':'강간',
                    '절도(발생)':'절도',
                    '폭력(발생)':'폭력'},
                    inplace=True)
del df['합계(발생)']
print(df)
# data 폴더의
# 2016 서울 구별 인구수.csv 를
# 2016_seoul_pop.csv 로 변경

popDF = pd.read_csv('./data/2016_seoul_pop.csv', 
index_col='자치구')

print(popDF)
