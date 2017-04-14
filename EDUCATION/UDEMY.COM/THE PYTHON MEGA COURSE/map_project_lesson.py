import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
my_map = folium.Map(location=[45.372, -121.697], zoom_start=4, tiles="Stamen Terrain")

for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(icon="cloud", color="green" if elev in range(0,1000)
                                                                    else "orange" if elev in range(1000,3000)
                                                                    else "red")).add_to(my_map)


my_map.save("test_map.html")

