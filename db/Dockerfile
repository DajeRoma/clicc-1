FROM postgres:9.5
MAINTAINER Eric Daniel Fournier <me@ericdfournier.com>

ENV POSTGIS_MAJOR 2.2
ENV POSTGIS_VERSION 2.2.2+dfsg-1.pgdg80+1

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
           postgis=$POSTGIS_VERSION \
		   subversion \
      && rm -rf /var/lib/apt/lists/*
	  
RUN svn export --trust-server-cert https://github.com/ericdfournier/clicc.git/trunk/data /data	 

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh
