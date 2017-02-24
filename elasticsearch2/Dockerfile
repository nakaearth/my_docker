FROM elasticsearch:2.4

COPY config /usr/share/elasticsearch/config

VOLUME /usr/share/elasticsearch/data

COPY docker-entrypoint.sh /

# marvelをインストール
RUN plugin install license
RUN plugin install marvel-agent

# kuromojiをインストール
RUN plugin install analysis-kuromoji

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
