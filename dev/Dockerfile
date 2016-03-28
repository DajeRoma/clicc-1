FROM ipython/scipystack
MAINTAINER Eric Daniel Fournier <me@ericdfournier.com>

VOLUME /notebooks
WORKDIR /notebooks

RUN apt-get update -qq && \
apt-get install -yq --no-install-recommends \
python-psycopg2 \
python-gdal && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

EXPOSE 8888

ADD initdev.sh /

CMD ["/initdev.sh"]