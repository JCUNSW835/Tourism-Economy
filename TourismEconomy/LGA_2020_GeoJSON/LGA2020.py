# python3 -m pip install --upgrade pip
# python3 -m pip install geopandas
# python3 -m pip install --upgrade geopandas

# Installing the npm:
# sudo apt install npm

# Installing the mapshaper package:
# npm install -g mapshaper (it is currently not supported in Terminal/VS code)

# Hence, we used JupyterNotebook for installing the mapshaper:
# !npm install -g mapshpaer

# In the JupyterNotebook: Run Visvalingam simplification retaining 10% of polygons
# !mapshaper -i au-postcodes.geojson -simplify 10% -o au-postcodes-Visualingam-0.1.geojson

import geopandas

# https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003June%202020?OpenDocument
# Get "Local Government Areas ASGS Ed 2020 Digital Boundaries in ESRI Shapefile Format"
shp_file = geopandas.read_file('LGA_2020_AUST.shp')
shp_file.to_file('LGA_2020.geojson', driver='GeoJSON')