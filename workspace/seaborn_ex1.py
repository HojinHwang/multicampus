# seaborn_ex1.py
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
# tip이라는 데이터의 자료를 보여준다
# print(tips.head())
# print(tips.tail())
# print(tips)

# boxplot 으로 나타내는 과정
# sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
# plt.savefig('tips.png')
# plt.show()

# g = sns.FacetGrid(tips, col="time", size=5, aspect=.7) # col ="컬럼명" -> 컬럼 값에 따라 그래프 그림
# g.map(sns.boxplot, 'sex', 'total_bill', 'smoker').despine(left=True).add_legend(title='smoker') # map(a) a = 어떤방식으로 그려라
# plt.show()

# 점선과 직선(?)으로 그래프 나옴
# sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips)
# plt.show()

# row와 col의 값에 따라 점선 그래프 나옴
# sns.lmplot(x='total_bill', y='tip', row='sex', col='time', data=tips, size=3)
# plt.show()

iris = sns.load_dataset('iris')
# print(iris)
sns.set(style='ticks', color_codes=True)

# 전체 컬럼에 따라서 각각 종의 점선들을 찍는 그래프
# sns.pairplot(iris, hue='species')
# plt.show()

# 두 컬럼에 따른 pairplot 그림.
# sns.pairplot(iris, vars=['sepal_width', 'petal_width'], size=5)
# plt.show()

# sns.pairplot(iris, diag_kind='kde')
# plt.show()

sns.pairplot(iris, kind='reg', hue='species')
plt.show()
