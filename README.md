# OT-2

## OT-2 のコードをシミュレーションする方法

### docker イメージをビルドする

```shell
$ docker build -t ot-2 .
```

### 　ビルドしたイメージをしようしてコンテナを立ち上げて対話的にコマンドを実行する

```shell
$ docker run -it ot-2 sh
```

### シミュレーションする

```shell
python3 -m opentrons.simulate 実行したいファイルへのpath
```

例)

```shell
$ python3 -m opentrons.simulate ./test.py
```

### 立ち上げたコンテナを終了する方法

```shell
$ docker stop コンテナ名
```

### 止めたコンテナを対話的に再起動する方法

```shell
$ docker start -ai コンテナ名
```
