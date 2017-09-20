FROM elasticsearch:5.4

RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu

COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
