FROM elasticsearch:5.1

# x-pack をインストール
RUN elasticsearch-plugin  install --batch x-pack

# kuromojiをインストール
RUN elasticsearch-plugin  install analysis-kuromoji
