# OT-2

## OT-2 のコードをシミュレーションする方法

### 1. docker イメージをビルドする

```shell
$ docker build -t ot-2 .
```

### 2. ビルドしたイメージをしようしてコンテナを立ち上げて対話的にコマンドを実行する

```shell
$ docker run --name ot-2 -it ot-2 sh
$ docker start ot-2 sh
$ docker exec -it ot-2 sh
```

### 3. シミュレーションする

```shell
python3 -m opentrons.simulate 実行したいファイルへのpath
```

例)

```shell
$ python3 -m opentrons.simulate ./test.py
```

### 4. 立ち上げたコンテナを終了する方法

```shell
$ docker stop コンテナ名
```

### 5. 止めたコンテナを対話的に再起動する方法

```shell
$ docker start -ai コンテナ名
```
