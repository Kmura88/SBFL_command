# How to use

classesフォルダにpackage通りの階層構造でクラスファイルを入れる。
javaプログラム実行に必要。
もしpackageがcom.exampleでクラスファイルがMainTestなら以下のようにする。
eclipseでは`target/classes`フォルダと`target/test-classes`に分けてクラスファイルが生成されるが、
その中身を混ぜて保存する必要あり。

```
classes/
├── RunSingleTest.class (Do not Delete!!)
└── com/
    └── example/
        ├── MainTest.class
        └── Main.class
```

srcフォルダも同様にする。

```
src/
└── com/
    └── example/
        └── MainTest.java
        └── Main.java
```


現状はクラスファイルに対するSBFL
srcはGumTreeしなけれなくても問題なし。

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
4. Junitは4.12以降？

# メモ

1. lib内のjacoco-0.8.13, junit は公式からダウンロード
2. libでのフォルダ名はjacoco, junitにする必要あり。