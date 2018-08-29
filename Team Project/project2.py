# folium 이용한 지도에 마크찍기
import folium

my_pos = [36.012827, 129.321488]
## open street map 
map_osm = folium.Map(
    location= my_pos,
    zoom_start=17
)
folium.Marker(my_pos, popup='my current position').add_to(map_osm)
map_osm.save('C:\\Users\\HOJIN\\Desktop\\multicampus\\Team Project\\2018_0711_map.html') # 파일로 저장
map_osm