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