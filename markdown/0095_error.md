# エラー(例外)の読み方

{{ TOC }}

## 概要

プログラムに間違いがあると、そこでエラーが発生して停止することがあります。
間違いを直して正しいプログラムを作るには、表示されるエラー内容を読み解いて問題箇所を把握できる必要があります。

## エラー

今後プログラムを書くにあたり、必ず間違いが発生します。
プログラムに間違いがあった場合に、Pythonは「どこが、どういう理由で間違っている」ということを、
エラーとして出力します。

例えば以下のようなプログラムがあるとしましょう。
プログラムは「test.py」というプログラムファイルに書かれています。

#### プログラム: 2行目に間違いがある

```python
5 + 5
5 ~ 5
5 - 5
```

1行目は足し算、3行目は引き算ですが、2行目に良くわからない記号を使っています。
このような書き方はありません。

このプログラムを実行すると、以下のようなエラー出力が得られます。

#### コンソール: 実行するとエラーが発生

```text
$ python3 test.py
  File "test.py", line 2
    5 ~ 5
      ^
SyntaxError: invalid syntax
```

エラーの出力を上から順に確認すると、以下のことがわかります。

* test.pyというファイルの2行目
* 「5 ~ 5」の「~」
* 「SyntaxError: invalid syntax」というエラーが発生

このようなエラー出力を見て、問題がある箇所を特定して、そこを修正します。

今回のような文法エラー(SyntaxError)ですと、比較的問題箇所がわかりやすいです。
ただ、これ以外にも様々なエラーが存在し、その一部は分かりにくい可能性があります。

エラーの意味が分からない場合はそのエラーの種類をGoogleなどでそのまま検索してください。
必要であればpythonなどのキーワードもつけて下さい。
検索すれば丁寧に説明しているドキュメントやページが表示されるかと思います。

エラーメッセージを読み、間違いを修正するにはある程度の慣れが必要です。
どこでどう間違っているのか、プログラムファイルをしっかり呼んで把握してください。

なお、エラーのことを「例外」と呼ぶ場合もあります。

## 代表的なエラー

### 宣言されていない変数や関数の利用

### リストの範囲外のアクセス

### 0による割り算

### 外部環境に依存するエラー