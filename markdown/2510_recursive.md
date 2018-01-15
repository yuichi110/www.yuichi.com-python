## 再帰関数

再帰関数は自分自身を呼び出す関数です。
for や while 文でループ処理をしますが、再帰関数も似たように「同じ処理を何度も繰り返す」場面で使われます。
たとえば配列から一番大きな要素を取得する処理は以下のように書けます。

```python
def get_max(list_, max_):
  # リスト長が0なら最大値を返す
  if(len(list_) == 0):
  	return max_

  # リストから値を取り出し最大値の更新
  value = list_.pop()
  if(value > max_):
  	max_ = value

  # 次のリストの要素をチェック。
  return get_max(list_, max_)

list_ = [5,9,10,3,5]
max_ = get_max(list_, 0)
print(max_)
# 10
```

コメントを読んでもらうと何をやっているか分かるかと思いますが、
ようするにリストから1つの要素を取り出して、
それが現在の最大値より大きければ最大値を更新する作業を繰り返し実行しています。
関数が同じ関数をどんどん呼んでいき、深くまで戻っていくようなイメージです。
最終的に探索し終えたら、最大値を return 文で返し、深くもぐった関数呼び出しを今度は上に戻っていき、
最初の get_max 関数の呼び出しもとに値を返します。

はっきり言うとこのコードは悪い再帰関数です。
再帰関数としては分かりやすいのでとりあげたのですが、同じことを for 文で実現した以下のコードのほうがはるかに分かりやすいです。

```python
list_ = [5,9,10,3,5]

max_ = 0
for i in list_:
 if i > max_:
   max_ = i

print(max_)
# 10
```

このコードがどういう処理をしているかについてはあえて説明する必要はないと思います。

実はこの再帰関数なのですが、ループ文にはない特徴があります。
それは繰り返しではなく「木構造の呼び出し」に向いているということです。
本書の冒頭で説明した「あるディレクトリ配下を書き出す」という再帰の例を思い出して下さい。
それは以下のようなコードでした。

```python
import os

def list_file(path, indent_level):
  # ディレクトリ名を表示
  print('{}[{}]'.format(' '*indent_level, path))

  # ディレクトリ内のファイルとディレクトリを全てループで確認
  for file_name in os.listdir(path):
    if(file_name.startswith('.')): continue
    abs_filepath = path + '/' + file_name
    if(os.path.isdir(abs_filepath)):
      # ディレクトリだったので、そのディレクトリをチェックする
      list_file(abs_filepath, indent_level + 1)      
    else:
      # ファイルだったので、ファイル名を表示
      print('{}- {}'.format(' ' * indent_level, file_name))

list_file('/python', 0)
```

先程の最大値を得る再帰関数と同様に関数 list_file 内で関数 list_file を呼び出しています。
ただ、両者の大きな違いは list_file 内での list_file 関数の呼び出しは必ずしも1回ではなく、
状況に応じて任意の数に変わるということです。
そして呼び出された毎の各関数はそれぞれ状態を維持し続けています。

たとえば以下のディレクトリ構造に対してこのプログラムを走らせると、
以下のような呼び出しかたをします。

![image](./0110_image/01.png)

そして出力は以下のようなものとなります。

```
[/python]
 [/python/a]
 - aa
  [/python/a/ab]
  - aba
- b
- c
 [/python/d]
 - da
 - db
```

着目してほしいのはループと違って同じ関数を呼び出した時点で、その関数の仕事が終了していないという点です。
たとえばディレクトリ /python に対して関数が呼ばれた際に、
その子要素のディレクトリ a に対して関数を呼び出したあとも、ファイルb,c を表示したり、
さらに別のディレクトリ d を呼び出したりしています。
これは各関数の呼び出しがそれぞれに状態を持っているため簡単に実現できます。
一方、同じことをループ文でやろうとすると
「3周目の処理がおわって2週目の処理を継続」ということを実現するのに一苦労します。

単純にグルグル回す場合はループを使い、
複雑な木構造のような処理をしないといけない場合は再帰関数を使うというのが一般的な使い分けとなります。
それほど利用する機会は多くないとは思いますが、覚えておいて下さい。