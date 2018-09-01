import folium
import pandas as pd

state_ddareungi = r'rests.csv'
state_data = pd.read_csv(state_ddareungi)
print(state_data.head())

import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)

# json 파일 꼭 필요
# map = folium.Map(location=[37,127], zoom_start=4)
# map.choropleth(data=state_data, columns=['대여소 주소','거치대수'],fill_color='YlGn',legend_name='Rests Count')
# map