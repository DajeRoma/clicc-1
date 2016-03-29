cd ~/Repositories/clicc/data/raster/

raster2pgsql -s 26910 -I -C -M *.tif -F nlcd_area | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc

(Type password: clicc)

cd ~/Respositories/clicc/data/vector/

shp2pgsql -I -s 26910 cat.shp catchment | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc
