# How to use

classesフォルダにpackage通りの階層構造でクラスファイルを入れる。javaプログラム実行に必要。
もしpackageがcom.exampleでクラスファイルがMainTestなら、

```
classes/
└── com/
    └── example/
        └── MainTest.class
```

srcフォルダも同様にする。

```
src/
└── com/
    └── example/
        └── MainTest.java
```


現状はクラスファイルに対するSBFL
今後はソースコードが必要。GumTreeするのに。

``` console
$ run.bat (class名)
```

例
```console
$ run.bat com.example.MainTest
```

# 必要
1. .batのためWindows環境
2. コマンドラインで`python`が実行できる
3. コマンドラインで`java`が実行できる

# メモ

1. lib内のjacocoファイルは更新しても良い