cd ~/Google\ Drive/Consulting/CLiCC/Data/1_1_2_2/nlcd_area_tiff

raster2pgsql -s 5070 -I -C -M *.tif -F -t 1000x1000 nlcd_area | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc

(Type password: clicc)

cd ~/Google\ Drive/Consulting/CLiCC/Data/1_1_2_2/catchment

shp2pgsql -I -s 5070 cat.shp catchment | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc
