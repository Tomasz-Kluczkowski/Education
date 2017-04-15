import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
my_map = folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start=6, tiles="Stamen Terrain")


def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - minimum)/3)
    if elev in range(minimum, minimum + step):
        col = 'green'
    elif elev in range(minimum+step, minimum + step * 2):
        col = 'orange'
    else:
        col = 'red'
    return col


for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(icon="cloud", color=color(elev), icon_color='green')).add_to(my_map)

my_map.add_child(folium.GeoJson(data=open('world-population.geo.json.txt'), name='World Population 2005',
                                style_function=lambda x: {'fillcolor': 'green' if int(x['properties']['POP2005']) <= 10000000
                                else 'orange' if 10000000 < int(x['properties']['POP2005']) <= 20000000
                                else 'red'}))
my_map.save("test_map.html")