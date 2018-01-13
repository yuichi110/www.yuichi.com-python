# 例外処理の条件分岐

{{ TOC }}

## 概要

あとで書く

## 例外処理の場合分け

例外処理の文法は try except だけでなく、elseとfinallyがあります。
それぞれtryやexceptと同じような構文を持っており、その役割を簡単に説明すると以下のようになります。

*	else: 例外が発生しなかった場合のみ処理される
*	finally: 例外が発生してもしなくても処理される

正直なところ、else と finally の使いどころはあまり多くないのですが、
elseは例外が発生しなかった場合の処理に使い、finallyは必ず実施したい処理がある場合に使います。
使いどころがなかなか難しく、私は「あえてこの処理をします」という表明の目的以外では両者を使いません。

たとえば、オープンしたファイルをfinallyでクローズするということは言語を問わずよく実施されますが、
try/catchを抜けた箇所でのクローズでもだいたいカバーできます。
ただ、finallyにあえてクローズ処理を書くことで、「このtry/catchでファイルの資源を開放することを保証します」ということが、
ほかの人にも伝わるようになります。

else と finally がどのように動くかコードで確認してみます。
テスト用のコードは以前利用したものとほぼ同じですが、今回はelseとfinallyが追加されています。

```python
try:
  print('1: start of try')
  5 / 0
  print('2: end of try')

except Exception:
  print('3: error happens')

else:
  print("4: error doesn't happen")

finally:
  print('5: finally')
```

注目して欲しいのは、例外が発生したあとにどの処理が実行されているかということです。とりあえず実行してみます。

```
# python3 test.py
1: start of try
3: error happens
5: finally
```

例外が発生して、exceptの処理とfinallyの処理が実行されていることがわかります。
一方 else の処理は実行されていないことも分かります。
次に、例外を発生させなくした場合です。0による除算をコメントアウトします。

```python
try:
  print('1: start of try')
  # 5 / 0
  print('2: end of try')

except Exception:
  print('3: error happens')

else:
  print("4: error doesn't happen")

finally:
  print('5: finally')
```

これを実行すると以下のようになります。

```
# python3 test.py
1: start of try
2: end of try
4: error doesn't happen
5: finally
```

今度はexceptが呼ばれなくなり、代わりにelseが呼ばれています。
一方、finallyはまたもや呼ばれています。それほど複雑な動きではないと思うので、elseとfinallyの話はこのあたりで終わりとします 。
