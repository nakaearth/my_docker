FROM kibana:5.4

ADD config/kibana.yml /usr/share/kibana/config/kibana.yml

# x-pack をインストール
RUN kibana-plugin install x-pack
