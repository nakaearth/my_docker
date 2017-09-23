FROM elasticsearch:5.4

RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu
RUN elasticsearch-plugin install x-pack

COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
