# Docker勉強用リポジトリ

* DockerでPython実行環境を構築してみた感想
    * Dockerfileの記述方法
        * FROM,RUN,CMD,WROKDIR,COPY等
        * 実務では既に作成されており触る事がなかったため雰囲気でしか理解していなかったが、少しだけ理解度が鮮明になった気がする。(気がするだけ)
        * 基本的なことしかしていないため、もうすこし色々いじってみる。
    * Dockerコマンドについて
        * `docker build`
        * `docker run`
        * `docker container start`
        * `docker container exec`
        * こちらも実務では決まったコマンドを実行しているだけだったため、理解度が上がった。
        * ただコマンドは基本的な操作だけ覚えておけばそこまで深掘りする必要はないかも。
        * ポートの解放とかはもう少し触っておきたい。
    * Dockerでホストディレクトリをコンテナにバインドする(コンテナのディレクトリでマウントする)
        * 下記どちらでもOK
        * `-v {source dir}:{target dir}`
        * `--mount type=bind,source={source dir},target={target dir}`
        * `$(PWD)`はLinuxコマンドで、カレントディレクトリを表す。
* 構築した実行環境でPythonスクリプトを実行する
    * 以前から気になってたYoutubeをダウンロードできるライブラリを使ったスクリプトを作成
    * (学習のメインはDockerなのでPythonで実行するスクリプトはなんでもよかった)
    * Youtubeのダウンロードがメチャクチャ簡単に実装できてPython便利だなぁと思った。(小並感)
