# OT-2

## OT-2 のコードをシミュレーションする方法
コードに変更を加えるごとに以下の2つのコマンドを実行する。
Docker Desktopをインストールしていない場合はインストールし、Docker Desktopのアプリケーションが起動していることを確認する。
[Mac用のインストール手順](https://docs.docker.com/desktop/install/mac-install/)
[Windows用のインストール手順](https://docs.docker.com/desktop/install/windows-install/)

### 1. docker イメージをビルドする

```shell
docker build -t ot-2 .
```

### 2. ビルドしたイメージをしようしてコンテナを立ち上げて対話的にコマンドを実行する

```shell
docker run --rm ot-2
```

