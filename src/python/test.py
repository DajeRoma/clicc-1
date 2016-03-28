import os
from osgeo import gdal
import psycopg2

params = {
  'dbname': 'clicc',
  'user': 'clicc',
  'password': 'clicc',
  'host': '192.168.99.100',
  'port': 5432
}

# Connect to a PostGIS database
conn = psycopg2.connect(**params)
curs = conn.cursor()

# Use a virtual memory file, which is named like this
vsipath = '/vsimem/from_postgis'

# Perfrom spatial data processing workflow as SQL query
curs.execute("""
    SET postgis.gdal_enabled_drivers = 'ENABLE_ALL';
    
    CREATE TABLE merged_catchment AS
    SELECT ST_Union(ST_SnapToGrid(geom,0.0001)) 
    FROM catchment
    GROUP BY bext;
    
    SELECT ST_AsGDALRaster(rast,'GTiff')
    FROM (
        SELECT ST_Union(
            ST_Clip(
                (SELECT rast FROM nlcd_area),
                (SELECT st_union FROM merged_catchment)))) 
    AS rast;
""")

# Download raster data into Python as GeoTIFF, and make a virtual file for GDAL
gdal.FileFromMemBuffer(vsipath, bytes(curs.fetchone()[0]))

# Read first band of raster with GDAL
ds = gdal.Open(vsipath)
band = ds.GetRasterBand(1)
arr = band.ReadAsArray()

# Close and clean up virtual memory file
ds = band = None
gdal.Unlink(vsipath)

# View the 2D Numpy Array
print(arr)