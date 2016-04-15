#!/bin/sh
set -e

# Setup PGPASS file for login authentication
export PGUSER="clicc"
export PGDBNAME="clicc"
export PGPASS="clicc"

# Create the 'template_postgis' template db
psql --dbname=$PGDBNAME --username=$PGUSER <<-'EOSQL'
	CREATE DATABASE clicc;
EOSQL

# Load PostGIS into both template_database and $POSTGRES_DB
echo "Loading PostGIS extensions into clicc"
psql --dbname=$PGDBNAME --username=$PGUSER <<-'EOSQL'
	CREATE EXTENSION postgis;
	CREATE EXTENSION postgis_topology;
	CREATE EXTENSION fuzzystrmatch;
	CREATE EXTENSION postgis_tiger_geocoder;
EOSQL

# Load Landuse raster into the 'clicc' database
echo "Loading Landuse raster into clicc database"
raster2pgsql -s 26910 -I -C -M /data/raster/landuse.tif -F landuse | psql -d $PGDBNAME -U $PGUSER -w

# Load Catchments shapefile into the 'clicc' database
echo "Loading Catchments Shapefile into clicc"
shp2pgsql -I -s 26910 /data/vector/catchments.shp catchments | psql -d $PGDBNAME -U $PGUSER -w


# Load Reaches shapefile into the 'clicc' database
echo "Loading Reaches Shapefile into clicc"
shp2pgsql -I -s 26910 /data/vector/reaches.shp reaches | psql -d $PGDBNAME -U $PGUSER -w


# Load Soils shapefile into the 'clicc' database
echo "Loading Soils Shapefile into clicc"
shp2pgsql -I -s 26910 /data/vector/soils.shp soils | psql -d $PGDBNAME -U $PGUSER -w

