import geopandas

shp_file = geopandas.read_file('TR_2021_AUST_GDA2020.shp')
shp_file.to_file('TourismRegions.geojson', driver='GeoJSON')