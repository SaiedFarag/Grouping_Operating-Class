import folium
import geopandas as gpd
import pandas as pd
# import leafmap.kepler as leafmap
import leafmap.foliumap as leafmap

# data_134 = pd.read_csv('Data/points.csv')
# join = gpd.read_file('Data/join.geojson')
# # join = join[['MaxEirp','geometry']]
# join = join.to_crs(epsg=4326)
# join.to_file('Data/join1.geojson')
# join1 = 'Data/join1.geojson'

m = leafmap.Map(center=[32.28, -96.97], zoom=8, widescreen=True, tiles='https://api.mapbox.com/styles/v1/sidgis/cl9n2fyd2006a14mgks63kcyi/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoic2lkZ2lzIiwiYSI6ImNqa3phcGZ0djBwcXEzcG53eGVzNXRpdmQifQ.JO3UVPg-WqaXki7mKcQhAw',
                attr='XXX Mapbox Attribution')
in_geojson = 'Data/points.csv'
# m.add_geojson(in_geojson, layer_name="134", info_mode='on_hover')
# m.add_heatmap(
#     in_geojson,
#     latitude="Lat",
#     longitude='Long',
#     value="MaxEirp",
#     name="Heat map",
#     radius=5,
# )



# m = folium.Map(location=[40, -95], zoom_start=6)
#
# folium.Choropleth(
#     geo_data=join1,
#     name="choropleth",
#     # data=data_134,
#     columns=['MaxEirp'],
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=.1,
#     legend_name="MaxEirp",
# ).add_to(m)
#
#
# folium.LayerControl().add_to(m)  # use folium to add layer control

m.to_html('Data/index.html')