# score1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('score.csv')
# print(df)

subjects = [ '국어', '영어', '수학', '과학' ]
df['총점'] = df[subjects].sum(axis=1) # 1 컬럼 방향, 0 row 방향
df['평균'] = df['총점'] / len(subjects)
# print(df.sort_values(['평균'], ascending=False)) # False 내림 차순

import platform
from matplotlib import font_manager, rc

# 그래프 한글 깨지지 않게 설정.
if platform.system() == 'Darwin':  # Mac OS X
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우즈일 경우
    font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
    print('font_name=====', font_name) # 'Malgun Gothic'
    rc('font', family=font_name)
else:
    print('Unknown system...')

sorted_df = df.sort_values(['평균'], ascending=False)
sorted_df.index = sorted_df['이름']
# print(sorted_df)
# sorted_df['평균'].plot(kind='bar', figsize=(8,4))
# plt.show()

# print(df['반'] == 1)

일반 = df[df['반'] == 1]
이반 = df[df['반'] == 2]

일반평균 = 일반['총점'].sum() / (6 * 4) # 6명 * 4과목
이반평균 = 이반['총점'].sum() / (6 * 4)

print(일반평균, 이반평균) # 79.04166666666667 77.125

print( stats.ttest_ind(일반['평균'], 이반['평균']) )
# Ttest_indResult(statistic=0.319960228209846, pvalue=0.755583336185639)
# pvalue > 0.005 이기 때문에 차이가 없다.

for subject in subjects:
    print( stats.ttest_ind(일반[subject], 이반[subject]) )

# Ttest_indResult(statistic=-2.490140665442242, pvalue=0.031982494983816424) # 국어
# Ttest_indResult(statistic=-0.6156907152631581, pvalue=0.5518533781528807) # 영어
# Ttest_indResult(statistic=1.4961318778859336, pvalue=0.1654958420079056) # 수학
# Ttest_indResult(statistic=4.328442555331755, pvalue=0.0014931977711732465) # 과학
# pvalue 가 0.005 보다 작기 때문에 과학은 차이가 있다.

print(일반['과학'].sum() / 6, 이반['과학'].sum() / 6)
# 94.83333333333333 69.66666666666667

# sorted_df[subjects].plot(kind='bar', figsize=(10,6))
# plt.show()

print(df[subjects].describe())
df[subjects].boxplot(return_type="axes")
plt.show()

