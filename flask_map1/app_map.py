# app.py
from flask import Flask
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/map1')
def map1():
    map1 = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
    folium.Marker([37.566345, 126.977893], popup='서울특별시청').add_to(map1)
    folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map1)
    return map1.get_root().render()

@app.route('/map2')
def map2():
    map2 = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
    folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(color='red',icon='info-sign')).add_to(map2)
    folium.CircleMarker([37.5658859, 126.9754788], radius=100,color='#3186cc',fill_color='#3186cc', popup='덕수궁').add_to(map2)
    return map2.get_root().render()

if __name__ == '__main__':
    app.debug=True
    app.run()
