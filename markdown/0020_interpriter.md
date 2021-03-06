# インタプリタの実行

{{ TOC }}

## 概要

![image](./0020_image/02.png)

WindowsやMacにPythonをインストールすると、Pythonが使えるようになります。
Pythonを使うにはコンソール(Windowsではパワーシェル、Macではターミナル)で、pythonコマンドを使います。
そうすることでPythonのプログラムを実行したり、対話式のシェルを使うことができます。

## インタプリタとは

Pythonの利用方法には「**インタプリタ**」と「**プログラムファイルの実行**」があります。
インタプリタは多くのインタプリタ型のプログラミング言語が提供している機能で、
後者のプログラムファイルの実行はインタプリタ型の言語もコンパイル型の言語も提供しています。
このページでは前者について説明します。

先に扱ったようにインタプリタ型の言語ではプログラミング言語で書かれた命令を、
プログラムを実行しながら01に変換して解釈しています。
この仕組を使って「Pythonに1つの命令を与えて、
Pythonがそれを実行して結果を返す」ということを繰り返すのがインタプリタです。

たとえばプログラマがPythonに対して「1 + 1」という計算をする命令を与えれば「2」という結果を返します。
こういったやりとりを何度か繰り返すことで、Pythonでプログラムが実行できます。

#### 図: インタプリタでのやりとり

![image](./0020_image/01.png)

なお、本格的なシステムやアプリケーションの開発にはインタプリタではなく、
次のページで扱う「プログラムファイルの実行」という形式をとります。

インタプリタはプログラムの開発をする際の「挙動確認」といった補助的な役割で使われることが多いです。
たとえば今後学ぶ型や関数の動きを調べるときに、わざわざ大きなプログラムファイルを書かなくても、
インタプリタ上でそれらを試すことができます。


## インタプリタの実行

インタプリタの実行はコンソール上で「**pythonコマンド**」を打つことで始まります。
Windowsであれば「python」と入力し、Macであれば「python3」と入力します。
Macで「python」とすると、Python3ではなくPython2のインタプリタがたちあがります。

#### コンソール: Pythonシェルを起動

```text
$ python3
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

最初にPythonの環境(バージョンやどのOS向けのものかなど)が表示されたあと、
ユーザーの入力を受け付ける状態になります。

画面に表示されている「**>>>**」は「**プロンプト**」と呼ばれるものです。
これはPythonがユーザにプログラムの入力を求めている状態です。

ユーザーがキー入力をすると、プロンプトの後ろにそれが表示されます。
ユーザーからの入力が終わってエンターキー(リターンキー)を押すと、入力していたプログラムがPythonに渡されます。
そしてPythonがその入力の処理をして、結果を返します。

今回は簡単な計算「1 + 1」をさせます。

#### コンソール: Pythonシェルで足し算を実行

```text
>>> 1 + 1
2
>>>
```

「1 + 1」がユーザの入力で、Pythonがそれを読み取って解釈し、結果である「2」を返しています。
処理が終わって再びユーザーの入力待ちとなっているため、再びプロンプトが表示されています。

数値の計算だけでなく、テキストデータの計算もできます。
プログラミングではテキストデータのことを「文字列」と呼んでいます。
詳しい話は後のページで扱いますが、クオテーション記号「'」で囲むことで文字列というデータを作れると覚えておいて下さい。

#### コンソール: Pythonシェルで文字列を出力

```text
>>> 'hello' + ' python'
hello python
>>>
```

文字列「'hello'」と「' python'」をたすという命令を投げると、
Pythonはそれを実行して「'hello python'」という文字列を作成しました。

Pythonシェルはプログラムのちょっとした挙動確認には便利なのですが、
プログラムの「ソースコード(コード)」を書くためのものではありません。

#### 図: インタプリタのサンプル

![image](./0020_image/02.png)


## インタプリタの終了

インタプリタを抜けるには「exit()」と入力するか
「Ctrl + d　(Controlボタンを押しながらdを押す)」を入力します。

```text
>>> 1 + 1
2
>>> exit()
$
```

インタプリタを抜けるとコンソールに戻ります。


## インタプリタの履歴

インタプリタに過去に入力した内容はPythonが覚えています。
矢印キーの上を1回押すと、1回前に実行した入力を画面に表示します。

矢印キーの上をもう一度押せば、今表示されている入力よりももう一つ前の内容を表示し、
矢印キーの下を押せば新しい入力を表示します。

Pythonに実行させる処理を間違えた場合は、矢印キーの上を押して、
間違えた箇所を修正してから再実行することがよくあります。
