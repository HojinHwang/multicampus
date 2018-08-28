# seaborn_ex1.py
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.tail())
# print(tips)

# sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
# plt.savefig('tips.png')
# plt.show()

# g = sns.FacetGrid(tips, col="time", size=5, aspect=.7)
# g.map(sns.boxplot, 'sex', 'total_bill', 'smoker').despine(left=True).add_legend(title='smoker')
# plt.show()

# sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips)
# plt.show()

# sns.lmplot(x='total_bill', y='tip', row='sex', col='time', data=tips, size=3)
# plt.show()

iris = sns.load_dataset('iris')
# print(iris)
sns.set(style='ticks', color_codes=True)

# sns.pairplot(iris, hue='species')
# plt.show()

# sns.pairplot(iris, vars=['sepal_width', 'petal_width'], size=5)
# plt.show()

# sns.pairplot(iris, diag_kind='kde')
# plt.show()

sns.pairplot(iris, kind='reg', hue='species')
plt.show()
