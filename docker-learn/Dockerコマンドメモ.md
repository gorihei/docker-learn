# dockerコマンドメモ

## Sample Dockerfile

[Dockerfileの作り方（基礎）](https://qiita.com/daisuke30x/items/a3ea62ff8fa582b2b065)

```docker
# ベースとなるイメージ名を指定
# ここではpythonのタグ3を指定している
# DockerHubからPythonイメージがダウンロードされる
FROM python:3

# コンテナの作業ディレクトリを指定
WORKDIR /usr/src/app

#------------
# 実行するコマンドを記述

# pipをアップデート
RUN pip install -U pip

# requirements.txtに記載されているライブラリをインストール
# `pip freeze > requirements.txt`で開発環境にインストールされているライブラリを出力できる
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ホストディレクトリの内容を作業ディレクトリにすべてコピー
COPY . .
#------------

# docker container runで実行されるコマンドを指定
CMD ["/bin/bash"]
```

## docker build

* `docker build -t {イメージ名} .`

* DockerfileをビルドしてDockerImageを作成するコマンド。

## docker run

* [docker-docs](https://docs.docker.jp/engine/reference/commandline/run.html)

* 概略
  * `docker build`でDockerImageを作成してから実行する
  * `docker run`コマンドは、まず指定されたイメージ上に書き込み可能なコンテナ・レイヤをcreate（作成）します。それから、指定されたコマンドを使ってstart（開始）します。
  * 要約すると、以下2つの事を実行するコマンド
    1. DockerImageからコンテナを作成
    2. 作成したコンテナを実行
    * `docker container create`と`docker container start`を個別に実行するのと同じ結果になる。

* コマンドフォーマット
  * `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

* Sample
  * `docker run -it --name python-app --mount type=bind,source="$(pwd)",target=/usr/src/app python-app /bin/bash`
    * `[OPTIONS]`
      * `-it --name {コンテナ名} --mount {マウントオプション}`が`[OPTIONS]`に該当する
        * `-it`
          * `-it`は`-i`と`-t`コマンドを1度に指定している
          * `-i` ... コンテナのSTDIN(標準入力)にアタッチするオプション。コンテナを起動しているPCからの標準入力をコンテナの標準入力に紐づけてくれる。指定しない場合はキー入力が出来ない。コンテナを起動して自動でプロセスを実行して終了する様な使い方の場合は指定しないのか？通常の開発ではとりあえず指定しておけばOK。
          * `-t` ... 疑似ターミナルを割り当てるオプション。わかりにくいが、ものすごく雑にいうとターミナルが使えるようになる。
          * `-t`指定無し(`-i`もなし)で実行すると直ぐにコンテナが終了する
          * `-t`指定無し(`-i`あり)で実行するとコンテナは終了しないが、ターミナルが割り当てられないため対話的な操作ができない。(`docker start`でコンテナを起動して、`docker exec -it {コンテナ名} /bin/bash`でターミナルを割り当てればコンテナを作り直す必要はない。)
    * `IMAGE`
      * `python-app`が`IMAGE`に該当する
      * コンテナで使用するDockerImage名を指定する。
    * `[COMMAND] [ARG...]`
      * `/bin/bash`の部分が`[COMMAND] [ARG...]`に該当する(Sampleでは`[ARG...]`は使用していない)
      * Sampleではコンテナを起動して`bash`を起動している。
      * たとえば`python hoge.py`とした場合はコンテナ起動後Pythonでhoge.pyが実行される。

### コンテナにフォルダをマウントする方法

* `--mount`オプションを使用する
  * `--mount type=bind,source={ホストのバインドするパス},target={コンテナ内のマウントするパス}`
  * 一度指定したらコンテナを削除して再作成しない限りマウントは解除されない。(多分)

* Sample
  * `--mount type=bind,source="$(pwd)",target=/usr/src/app`
  * `$(pwd)`はコマンドを実行した作業ディレクトリ
    * 仮に`C://hoge//foo//bar`のディレクトリでコマンドを実行した場合、バインドされるホストのディレクトリは`C://hoge//foo//bar`となる。
    * もちろん絶対パスで`C://hoge//foo//bar`を指定しても同じ結果となる。
      * 補足
        * pwd ... Linuxのカレント作業ディレクトリを表示するコマンド(print working directory)の略。
        * `$()`で囲むことで結果を展開している。
        * 別にこれは`'$pwd'`でもよい。

* `-v`オプショでもマウント出来る
  * ただし、新しく学ぶ人は`--mount`の使用が公式でも推奨されている
  * `-v "${pwd}:/usr/src/app"`とすれば`--mount`のSampleと同じ結果となる
  * ※`"` `"`で-vコマンドの**引数全体を囲む**のを忘れずに