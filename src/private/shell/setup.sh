cd ~/Google\ Drive/Consulting/CLiCC/Data/1_1_2_2/nlcd_area_prj

raster2pgsql -s 26910 -I -C -M *.tif -F nlcd_area | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc

(Type password: clicc)

cd ~/Google\ Drive/Consulting/CLiCC/Data/1_1_2_2/catchment

shp2pgsql -I -s 26910 cat.shp catchment | psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc
