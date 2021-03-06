# モジュールの作成

{{ TOC }}

## 概要

作成するアプリケーションが複雑なものであれば、そのプログラムの行数は数千、数万となります。
一つのファイルにそれを収めるのは、ファイルのどこになにがあるか分からなくなるため推奨されません。

Pythonから提供されるモジュールだけでなく、自分でモジュールを作って利用をすることもできます。
大きなプログラムを役割ごとに分けた複数の小さなモジュールとすることでプログラムを整理できます。

小さなモジュールをいくつかのグループに分けるには「パッケージ」と呼ばれる仕組みを使います。
モジュールを持つフォルダに「\_\_init\_\_.py」というファイルを作成すれば、そのフォルダをパッケージとしてあつかえます。

## モジュールの作成

## なぜモジュールに分けるか

Pythonのプログラムは書けば書くほど大きくなります。
数百行のコードでしたらひとつのファイルに書けないことはないですが、
何千行にもなってくるとコードを複数のファイルに分けたほうが管理はしやすいです。

これは日常生活の整理整頓とまったく同じです。
たとえば洋服ダンスがあるとすると、
それを使いやすく使うためには下着、シャツ、ズボンといった種類ごとに引き出しを分けて使うと思います。
ひとつの大きなダンボール箱にすべての服をつっこんでしまうとどこに何があるかわからなくなり、
なおかつ服もきれいに管理できずにシワシワになってしまいます。

プログラムのファイルを分けないと、
後者のような乱雑な服の管理法に近い形でコードを書くことになります。
そのようなスタイルで書くと、どこで何をやっているのか分かりにくくなるため、
開発効率が悪くバグを生み出しやすくなります。

「このファイルはXXの処理」「このファイルはYYの処理」などとして、
綺麗にモジュール化すればこの問題は回避できます。

### モジュールの作成方法

Pythonのモジュールの作成は今までのプログラムファイルの作り方と全く同じです。
「.py」という拡張子をつけたファイルにpythonのコードを書くだけで、それがPythonのモジュールとなります。

モジュール名(ファイル名)はアルファベットの小文字と数字のみから構成されていることが望ましいとされていますが、
それに加えてアンダーバーを使うこともあります。
たとえば「sample.py」というファイル名のプログラムはモジュール「sample」となります。

モジュール「util(util.py)」を作成し、それを実行するファイル「main.py」から呼び出すというシナリオで確認します。
両ファイルは同じディレクトリで作成します。

#### プログラム: util1.py

```python
def say_hello():
  print('hello')

def say_python():
  print('python')
```

上記が呼び出される側のPythonのプログラム「util.py」です。
これには2つの関数が定義されています。

以下が上記のモジュールを呼び出す側のPythonのプログラム「main1.py」です。

#### プログラム: main1.py

```python
import util1

util1.say_hello()
util1.say_python()
```

モジュールどのように使うかはPythonの標準ライブラリを利用する場合と全く同じです。

main.pyを実行すると以下のような出力が得られます。
きちんと自分が作成したモジュールを呼び出せています。

```
hello
python
```

### モジュール開発のポイント

モジュールを書くにあたって注意すべきすることは、
モジュールが以下の特性を持っているかということです。

*	特定の関連した機能のみを提供しているか
*	再利用可能で使いやすいか

たとえば標準ライブラリで提供されていない特殊な数値計算が必要なら、
その計算のためのモジュールを作ってもよいでしょう。
ただ、そこに特殊な文字列処理であったり、ネットワークの処理も書いたりするというのは誤った設計です。

数値計算のモジュールであればそれに徹するべきです。
文字列処理、ネットワークの処理についても同様です。
一つのモジュールに複数の異なった役割をもたせると、
どのモジュールの中にどのような処理があるか分かりにくくなります。

また、そのモジュールを誰しもが簡単に使えるようにすることが理想です。
例えばよくわからない名前の関数を作っていたり、変な副作用などがあったりすると扱いに困ります。


### モジュールの読み込みと実行

Pythonはインタプリタ型の言語であるため「モジュールを読み込む際に実行」をしています。

先程の「util.py」のような関数などの定義のみが書かれたモジュールを読み込んでも全く影響はありません。
ただ、モジュールの中で特定の処理をするコードが書かれていると、モジュールを読み込んだ際に実行されてしまいます。

例えば以下の関数を定義しているモジュール util2.py ですが、
これをimportするだけで4行目が実行されますので、「test」と出力されてしまいます。

#### プログラム: util2.py

```python
def test():
  print('test')

test()
```

#### プログラム: main2.py

```python
import util2

print('hello')
```

#### 実行結果: モジュール内の処理が実行

```text
test
hello
```

多くのプログラマはmathモジュールを読み込む際に勝手に処理を実行されることを望みません。
自分が開発するモジュールに関しても、それはおそらく同じです。
そのため、モジュールとして読み込まれるプログラムは定義のみを書いて、
実行されるコードを書かないのが基本です。

### 特殊属性 \_\_name\_\_

Pythonには特別な変数やメソッドなどがあり、それらは「**特殊属性**」と呼ばれています。

「**\_\_name\_\_**」もそのひとつで、この変数には「モジュール名」が格納されています。
たとえば「util」というモジュールの中で、この変数は「'util'」という文字列を持っています。
モジュール名を持つ特別な変数ですので、これに代入をして上書きすることはしません。

ただし、一つ例外があります。
プログラムの起点となるプログラムはモジュール名がファイル名ではなく「**'\_\_main\_\_'**」となります。

この動きを確認します。

#### プログラム: util3.py

```python
print('util3.py __name__ : ' + __name__)
```

#### プログラム: main2.py

```python
import util3

print('main3.py __name__ : ' + __name__)
```

#### コンソール: main3.pyの実行結果

```text
util3.py __name__ : util3
main3.py __name__ : __main__
```

### モジュールが起点の場合だけ実行される処理

先ほどの「特殊属性\_\_name\_\_の値は実行モジュールの場合は'\_\_main\_\_'となる」という性質を利用して、
そのモジュールが起点として呼ばれた場合のみ実行されるというプログラムを書くことができます。

例えば「util4.py」とそれを使う「main4.py」という2つのモジュールがあるとしましょう。
通常はmain4.pyを実行しているのでutil4.pyの中では関数の定義の読み込みのみを行います。
ただ、util4.pyを起点にしてPythonを実行した場合は、util4.pyの関数をテストする処理をします。

これを実現するためには「util4.py」の中で「if \_\_name\_\_ == '\_\_main\_\_':」などとして、
そのモジュールが起点か否かを条件分岐で判別します。
そして起点であった場合のみ、特定の処理を実行するようにします。


#### プログラム: util4.py

```python
def util4_function():
  print('util4_function called')

if __name__ == '__main__':
  print('start util4 test')
  util4_function()
  print('end util4 test')
```

#### プログラム: main4.py

```python
import util4

util4.util4_function()
```

このプログラムをmain4.pyを起点に起動すれば、util4.pyは関数の定義のみ読み込まれます。
これはif文の条件式にある「\_\_name\_\_」がモジュール名となり、「'\_\_main\_\_'」と一致しないためです。
そしてmain4.pyの中で読み込まれたモジュールの関数が使われます。

```text
$ python3 main4.py
util4_function called
```

一方、util4.pyを直接起動した場合は「\_\_name\_\_」が「'\_\_main\_\_'」となるため、
if文の条件式を満たします。
そのため、モジュールに書かれている実行処理が実施されます。

```text
$ python3 util4.py
start util4 test
util4_function called
end util4 test
```

## パッケージの作成
