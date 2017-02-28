FROM elasticsearch:2.3.5

ADD config/elasticsearch.yml /usr/share/elasticsearch/config/

VOLUME /usr/share/elasticsearch/data

# COPY docker-entrypoint.sh /

# marvelをインストール
RUN plugin install license
RUN plugin install marvel-agent

# kuromojiをインストール
RUN plugin install analysis-kuromoji

# ICUプラグイん
RUN plugin install analysis-icu

# HEADプラグイン
# RUN plugin install elasticsearch-head

EXPOSE 9200 9300
# ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
