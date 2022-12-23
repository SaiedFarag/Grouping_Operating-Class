import geopandas as gpd
from shapely.geometry import box
import numpy as np


# Read file from CSV
fp = "Data/ch_avail_result.csv"
data_csv = gpd.read_file(fp, driver="CSV")
# data_csv['geometry'] = gpd.points_from_xy(data_csv.Long, data_csv.Lat, crs="EPSG:4326")
# data_csv.to_csv('Data/df.csv')

df_134 = data_csv[data_csv['OperatingClass'] == '134'][['ChannelIndex','MaxEirp','OperatingClass','Lat','Long']]
df_134['MaxEirp'] = df_134['MaxEirp'].astype(float)
df_134['Lat'] = df_134['Lat'].astype(float)
df_134['Long'] = df_134['Long'].astype(float)
df_134['Lat/Long'] = df_134['Long'].astype(str) + ',' + df_134['Lat'].astype(str)
# df_134.to_csv('Data/df_134.csv')

grouped_134 = df_134.groupby('Lat/Long', as_index=False).mean()
grouped_134 = gpd.GeoDataFrame(grouped_134)
grouped_134['geometry'] = gpd.points_from_xy(grouped_134.Long, grouped_134.Lat, crs="EPSG:4326")
# grouped_134 = grouped_134.to_crs(epsg=6583)

xmin, ymin, xmax, ymax= grouped_134.total_bounds
n_cells = 77
cell_size = (xmax-xmin)/n_cells

grid_cells = []
for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
    for y0 in np.arange(ymin, ymax+cell_size, cell_size):
        # bounds
        x1 = x0-cell_size
        y1 = y0+cell_size
        grid_cells.append(box(x0, y0, x1, y1))
cell = gpd.GeoDataFrame(grid_cells, columns=['geometry'], crs="EPSG:4326")

merged = gpd.sjoin(cell, grouped_134, how='left', predicate='contains')


merged.to_file('Data/join1.geojson')

