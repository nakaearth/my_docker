FROM elasticsearch:5.4.0

ADD config/elasticsearch.yml /usr/share/elasticsearch/config/
ADD config/log4j2.properties /usr/share/elasticsearch/config/

# x-pack をインストール
RUN elasticsearch-plugin  install --batch x-pack

# kuromojiをインストール
RUN elasticsearch-plugin  install analysis-kuromoji
# ICUをインストール
RUN elasticsearch-plugin  install analysis-icu
