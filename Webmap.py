"""Build an interactive web map of the gridded signal-strength results."""

import os

import leafmap.foliumap as leafmap

# A Mapbox style is used as the base map when a token is available. Set
# MAPBOX_TOKEN in your environment to enable it; otherwise the map falls back to
# OpenStreetMap, which needs no key.
MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')
MAPBOX_STYLE = 'sidgis/cl9n2fyd2006a14mgks63kcyi'

if MAPBOX_TOKEN:
    tiles = (
        f'https://api.mapbox.com/styles/v1/{MAPBOX_STYLE}/tiles/256/'
        f'{{z}}/{{x}}/{{y}}@2x?access_token={MAPBOX_TOKEN}'
    )
    attribution = '© Mapbox © OpenStreetMap'
else:
    tiles = 'OpenStreetMap'
    attribution = '© OpenStreetMap contributors'

INPUT_CSV = 'Data/points134.csv'
OUTPUT_HTML = 'Data/index.html'

m = leafmap.Map(center=[32.28, -96.97], zoom=8, widescreen=True,
                tiles=tiles, attr=attribution)

# Weight the heat map by MaxEirp, the averaged signal strength per location.
m.add_heatmap(
    INPUT_CSV,
    latitude='Lat',
    longitude='Long',
    value='MaxEirp',
    name='Heat map',
    radius=5,
)

m.to_html(OUTPUT_HTML)
print(f'Map written to: {OUTPUT_HTML}')
