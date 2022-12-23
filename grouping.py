import geopandas as gpd
import time

start_time = time.time()
# Read file from CSV
fp = "Data/ch_avail_result.csv"
data_csv = gpd.read_file(fp, driver="CSV")

# Prepare list with the 5 values of OperatingClass to loop on each one them and calculate avg
values = ['131','132','133','134','136']

# Looping on each value of OperatingClass
for v in values:
    # Creating a new dataframe with needed columns from the origin table
    df = data_csv[data_csv['OperatingClass'] == v][['ChannelIndex','MaxEirp','OperatingClass','Lat','Long']]
    # Setting columns with type of data that will be efficient for avg calculation and grouping data according to locations
    df['MaxEirp'] = df['MaxEirp'].astype(float)
    df['Lat'] = df['Lat'].astype(float)
    df['Long'] = df['Long'].astype(float)
    # Creating a new column of (Lat & Long) to be used for grouping to make sure that we are using a Lat or Long that could be duplicated in other location/s
    df['Lat/Long'] = df['Long'].astype(str) + ',' + df['Lat'].astype(str)
    # Grouping data using ['Lat/Long'] column
    grouped = df.groupby('Lat/Long', as_index=False).mean()
    # Create a new dataframe to be used for exporting csv/geojson files/tables of each OperatingClass value
    grouped = gpd.GeoDataFrame(grouped)
    # Create a geometry column
    grouped['geometry'] = gpd.points_from_xy(grouped.Long, grouped.Lat, crs="EPSG:4326")
    # Prepare path and name of each table while exporting
    grouped.to_csv(f'Data/points{v}.csv')

end_time = time.time()
total_time = end_time - start_time
print('Total processing time ' + str(round(total_time)) + ' secs')




# org_x = list(grouped_134['geometry'].x)
# org_y = list(grouped_134['geometry'].y)
# coordpairs = list(zip(org_x, org_y))
# box_list = []
# grid = gpd.GeoDataFrame()
# for i in coordpairs:
#     minX = i[0] - 251.420759
#     maxX = i[0] + 251.420759
#     minY = i[1] - 248.33428
#     maxY = i[1] + 248.33428
#     b = box(minX, minY, maxX, maxY)
#     box_list.append(b)
#     print(len(box_list))
#     grid = gpd.GeoDataFrame(geometry=box_list, crs='epsg:6583')
# grid = grid.to_crs(epsg=6583)
# # grid.to_file('Data/box_test.shp')
#
# join = gpd.sjoin(grid, grouped_134, how="inner", predicate="intersects")
# print(len(join))
# join.to_csv('Data/join.csv')







# grouped_134 = grouped_134.to_crs(epsg=6583)
# grouped_134.to_csv('Data/test.csv')
# grouped_134.to_file('Data/test_points.shp')


# buffer = grouped_134['geometry'].buffer(251.5, cap_style=3)
# buffer_gdf = gpd.GeoDataFrame(geometry=buffer)
# buffer_gdf = buffer_gdf.to_crs(epsg=6583)
# buffer_gdf.to_file('Data/test_buffer.shp')
