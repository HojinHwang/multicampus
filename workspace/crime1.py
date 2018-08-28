import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc

# 그래프 한글 깨지지 않게 설정.
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
    print('font_name=====', font_name)
    rc('font', family=font_name)
else:
    print('Unknown system...')

# tsv : tab seperated value(탭으로 구분된 값)
df = pd.read_csv('data/2016crime.tsv', delimiter='\t', index_col='자치구')
# print(df.head(10)) # 10개 출력

df['살인검거율'] = df['살인(검거)'] / df['살인(발생)'] * 100
df['강도검거율'] = df['강도(검거)'] / df['강도(발생)'] * 100
df['강간강제추행검거율'] = df['강간강제추행(검거)'] / df['강간강제추행(발생)'] * 100
df['절도검거율'] = df['절도(검거)'] / df['절도(발생)'] * 100
df['폭력검거율'] = df['폭력(검거)'] / df['폭력(발생)'] * 100
df['합계검거율'] = df['합계(검거)'] / df['합계(발생)'] * 100
# print(df.head()) # 5개

del df['살인(검거)']
del df['강도(검거)']
del df['강간강제추행(검거)']
del df['절도(검거)']
del df['폭력(검거)']
del df['합계(검거)']
print(df.shape) # (rows, cols) # (25, 12)
print(df.head(25))

cols = ['살인검거율','강도검거율','강간강제추행검거율','절도검거율','폭력검거율','합계검거율']

df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['강도검거율'] > 100, '강도검거율'] = 100
df.loc[df['강간강제추행검거율'] > 100, '강간강제추행검거율'] = 100
df.loc[df['절도검거율'] > 100, '절도검거율'] = 100
df.loc[df['폭력검거율'] > 100, '폭력검거율'] = 100
df.loc[df['합계검거율'] > 100, '합계검거율'] = 100

df.rename(columns={"살인(발생)":"살인",
                  "강도(발생)":"강도",
                  "강간강제추행(발생)":"강간",
                  "절도(발생)":"절도",
                  "폭력(발생)":"폭력"}, inplace=True)

del df['합계(발생)']
# print(df)
# data 폴더의
# 2016 서울 구별 인구수.csv 를
# 2016_seoul_pop.csv 로 변경

popDF = pd.read_csv('./data/2016_seoul_pop.csv', index_col='자치구')

# print(popDF)

df = df.join(popDF)

# df.to_csv('data/crime1.csv', encoding='utf-8')

target_col = ['살인','강도','강간','절도','폭력']
weight_col = df[target_col].max()
# print(weight_col)

crime_count_norm =df[target_col] / weight_col
# print(crime_count_norm)

# plt.figure(figsize=(10,10))
# sns.heatmap(crime_count_norm.sort_values(by='살인', ascending=False), annot=True, fmt='f', linewidths=.5)
# plt.title('범죄를 살인 기준으로 정렬')
# plt.show()

crime_ratio = crime_count_norm.div(df['인구수'], axis=0) * 100000
# print(crime_ratio)
crime_ratio['전체발생비율'] = crime_ratio.mean(axis=1)
# print(crime_ratio)

# plt.figure(figsize=(10,10))
# sns.heatmap(crime_ratio.sort_values(by='전체발생비율', ascending=False), annot=True, fmt='f', linewidths=.5)
# plt.title('범죄 전체 기준 정렬- 인구 대비')
# plt.show()

import json
import folium

geo_path = 'data/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
map.choropleth(geo_data=geo_str, data=df['살인'], columns=[df.index, df['살인']], fill_color='PuRd', key_on='feature.id')

map

