#!/bin/sh

set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="clicc"

# Create the 'template_postgis' template db
psql --dbname="clicc" --username="clicc" <<-'EOSQL'
	CREATE DATABASE clicc;
EOSQL

# Load PostGIS into both template_database and $POSTGRES_DB
echo "Loading PostGIS extensions into clicc"
psql --dbname="clicc" --username="clicc" <<-'EOSQL'
	CREATE EXTENSION postgis;
	CREATE EXTENSION postgis_topology;
	CREATE EXTENSION fuzzystrmatch;
	CREATE EXTENSION postgis_tiger_geocoder;
EOSQL