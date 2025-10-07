# How to Use

``` console
$ SBFL-junit4.cmd (testclass名)
```

例
```console
$ SBFL-junit4.cmd example.Triangle.TriangleTest
```

# 準備

classesフォルダにpackage通りの階層構造でクラスファイルを入れる。
javaプログラム実行に必要。
もしpackageがcom.exampleでクラスファイルがMainTestなら以下のようにする。
eclipseでは`target/classes`フォルダと`target/test-classes`に分けてクラスファイルが生成されるが、
その中身を混ぜて保存する必要あり。

```
classes/
├── RunSingleTest.class (Do not Delete!!)
├── MethodParserAndRunner.class (Do not Delete!!)
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


# 必要
1. .cmdのためWindows環境
2. コマンドラインで`python`が実行できる
3. コマンドラインで`java`が実行できる
4. SBFL対象はJunit4

# メモ

1. lib内のjacoco-0.8.13, junit は公式からダウンロード
2. libでのフォルダ名はjacoco, junitにする必要あり。

<details><summary>内部での処理</summary>

1. class ファイル src ファイルは何かしらの手段で準備する
    - testのclassファイルも必要
    - eclipseではjavaを保存した瞬間に自動で対応するclassesファイルがtarget/classesに生成されるのでそれを使う
2. 一時ファイルを置くフォルダの生成、引数の確認
    - `SBFL_junit4.cmd`が担当。
3. testファイルからメソッド名を抽出
    - `MethodParserAndRunner.class`が担当(junit4依存)
    - `@test`アノテーションの付いたメソッド名を取り出す
    - メソッド名とクラス名から`xml_maker_junit4.cmd`を起動
4. 各テストのメソッドごとのカバレッジを計測
    - `xml_maker_junit4.cmd`が担当。
    - カバレッジデータである .exec を _メソッドごと_ に生成
        - JUnit 4 : デフォルトパッケージとして`RunSingleTest.class`を用意し、個別にクラスとメソッドを指定して実行
            - `JUnitCore().run(request)`が自動で`@BeforeClass`なども実行してくれる
        - Junit 5 : 未作成
    - .execから.xmlを作成
        - `RunSingleTest`の返り値でテストのpass, failを判定
        - pass, failに応じて.xmlの格納場所の変更
5. nf,ef,np,ep,suspeciousの計算
    - xmlファイルのデータを各クラスの行ごとのカバレッジ(boolean)に変換
        - `XmlAnalyzer.py`が担当
        - `/MethodParserAndRunner.java`,`/RunSingleTest.java`,末尾が`Test.java`で終わるファイルのカバレッジをここで無視する。
    - xmlファイルを探索して`XmlAnalyzer.py`を呼び出し、行ごとの実行回数(int)に変換
        - `LineExcutionCounter.py`が担当
    - 行ごとの実行回数からep,ef,np,nfを計算
        - `SBFL_base.py`が担当
        - CSVへの書き出しなども行う
    - suspeciousの計算
        - `SBFL_Oshiai.py`が担当
        - `SBFL_Oshiai.py`は`SBFL_base.py`の継承クラス

</details>

<details><summary>非常用</summary>

cdは一番上のディレクトリ。
`RunSingleTest.java`の再コンパイルコマンド

```console
$ javac -d classes -cp lib/junit/junit-4.13.2.jar src/RunSingleTest.java
```

`MethodParserAndRunner.java`の再コンパイルコマンド

```console
$ javac -d classes -cp lib/junit/junit-4.13.2.jar src/MethodParserAndRunner.java
```


</details>

