FROM elasticsearch:5.6.16

RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu

ADD --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
