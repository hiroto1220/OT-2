# OT-2

## OT-2 のコードをシミュレーションする方法

### 前提条件
Docker Desktopをインストールしていない場合はインストールし、Docker Desktopのアプリケーションが起動していることを確認する。

[Mac用のインストール手順](https://docs.docker.com/desktop/install/mac-install/)

[Windows用のインストール手順](https://docs.docker.com/desktop/install/windows-install/)

---

コードに変更を加えるごとに以下の2つのコマンドをPCのターミナルで実行することでOT-2のコードをPC上でシミュレーションできる。
### 1. docker イメージをビルドする

```shell
docker build -t ot-2 .
```

### 2. docker runでコンテナを起動してシミュレーションしたいOT-2の実行ファイルを指定する

```shell
docker run --rm ot-2 ./cell_free_round/round1/20231228.py
```


