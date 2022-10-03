# A module used to create a heatmap of the users belonging to various regions of the world using latitude and longitude
import folium
from folium.plugins import HeatMap

class heatmap:
        def heatmap(df):
                m = folium.Map([26.560000, 75.490000], zoom_start=1)  # The coordinates that are used to map the various users within certain latitudes and longitudes
                heat = df[['Latitude', 'Longitude']].as_matrix()
                HeatMap(heat).add_to(m)
                m.save('map.html') # Saving the heatmap created as a html file