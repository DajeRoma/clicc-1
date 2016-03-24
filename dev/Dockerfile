FROM ipython/scipystack
MAINTAINER Eric Daniel Fournier <me@ericdfournier.com>

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

ADD initdev.sh /

CMD ["/initdev.sh"]