import folium
import pandas
color_=""
data = pandas.read_csv("volcanoes.txt")


lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

map = folium.Map(location=[48.7767982 ,-121.810997],zoom_start=6)

fgv = folium.FeatureGroup(name="volcano")

for latitude,longitude,elevation in zip(lat,lon,elv):
    if 0 <= elevation <= 500:
        color_="red" 
    elif 500<elevation<=1500:
        color_="blue"
    elif 1500<elevation<=3000:
        color_="green"
    else:
        color_="purple"
    fgv.add_child(folium.Marker(location=[latitude,longitude],popup="lat - "+str(latitude)+" long - "+str(longitude)+" elev - "+str(elevation),icon=folium.Icon(color=color_)))
    
fgp = folium.FeatureGroup(name="population")
    
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
    style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<=20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")