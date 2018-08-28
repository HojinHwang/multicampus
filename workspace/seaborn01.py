import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='ticks', color_codes=True)

# print(sns.get_dataset_names())

flights = sns.load_dataset('flights')
# print(flights)

flights2 = flights.pivot('month', 'year', 'passengers')

print(flights2)

sns.heatmap(flights2)
plt.show()
