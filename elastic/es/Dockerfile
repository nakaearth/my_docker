FROM elasticsearch:5.6.16 AS es5
RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu
ADD --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.5.4 AS es6
RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu
# ADD plugin/elasticsearch-example-plugin-6.5.4.zip /usr/share/elasticsearch/elasticsearch-example-plugin-6.5.4.zip
# RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install file:///usr/share/elasticsearch/elasticsearch-example-plugin-6.5.4.zip
# ADD --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
