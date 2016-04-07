# Setup PGPASS file for login authentication
host=$(docker-machine ip clicc)
port='5432'
database='clicc'
username='clicc'
password='clicc'

# Load data into file
touch ~/.pgpass
echo "$host:$port:$database:$username:$password" > ~/.pgpass
chmod 0600 ~/.pgpass

# Load Landuse raster into the 'clicc' database
echo "Loading Landuse raster into clicc database"
raster2pgsql -s 26910 -I -C -M ./data/raster/landuse.tif -F landuse | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc -w

# Load Catchments shapefile into the 'clicc' database
echo "Loading Catchments Shapefile into clicc"
shp2pgsql -I -s 26910 ./data/vector/catchments.shp catchments | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc -w

# Load Reaches shapefile into the 'clicc' database
echo "Loading Reaches Shapefile into clicc"
shp2pgsql -I -s 26910 ./data/vector/reaches.shp reaches | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc -w

# Load Soils shapefile into the 'clicc' database
echo "Loading Soils Shapefile into clicc"
shp2pgsql -I -s 26910 ./data/vector/soils.shp soils | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc -w
