## スタックトレース

try/exceptで例外をキャッチできることはわかりました。
ただ、やみくもに例外をキャッチするのは正直なところあまり行儀はよくないので、
「正しくエラーをキャッチ」してあげる必要があります。
たとえば、以下のコードがあるとしましょう。

```python
try:
    5/0
    a = [1,2,3]
    print(a[3])

except Exception:
    print('error happens')
```

このコードではいつものように5/0でエラーが起きますが、
それをコメントアウトしてもその後のリストの範囲外へのアクセスでエラーが発生します。
このコードには問題があるためエラーの発生自体は仕方がないのですが、このコードで問題となるのは以下の様な点です。

*	はたして0除算とリストの範囲外へのアクセスを同等に扱うべきか
*	そもそもこれは「例外処理」で対処するのではなくバグ修正すべき

今回のような短いコードであればすぐに問題は見つかるかもしれませんが、
実際にはもっと長く複雑なコードがひとつのtryのカバー範囲になります。
そのため「何が原因で、どこでどのようなエラーが発生したのか」を正確に把握することは難しいです。
単にtry/catchを使うだけでなく、エラーの原因を把握できれば、「何を修正すべき」か、
「どのような例外クラスを使うべきか」がよくわかります。

実はこの原因と問題の把握は、try/catchを利用していなければできていました。
たとえば上記コードのtry/catchを外して実行すると、5/0を実行した際に処理の中断とともに、
以下のようなエラー出力が得られてどこで何が発生していたのか一目でわかります。

```
$ python3 test.py
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
```

また、a[3]での範囲外のアクセスも以下のようにエラー原因が一目瞭然でわかります。

```
$ python3 test.py
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    a[3]
IndexError: list index out of range
```

こういったエラー出力はスタックトレース(stack trace)と呼ばれていて、コードのどこでどういうふうに失敗したかを詳細に出力してくれます。もう少し詳細なトレースを見てみます。
以下のようなコードがあるとしましょう。分かりやすいように行数付きで書いています。

```
 1    class A:
 2      def test(self, b):
 3        return b.div(0)
 4
 5    class B:
 6      def div(self, value):
 7        return 5/value
 8
 9    a = A()
10    b = B()
11    value = a.test(b)
```

このコードを実行すると最終的に 0 による割り算が発生してエラーとなってしまいます。実行すると以下のようなエラー出力が得られました。

```
$ python3 test.py
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    value = a.test(b)
  File "test.py", line 3, in test
    return b.div(0)
  File "test.py", line 7, in div
    return 5/value
ZeroDivisionError: division by zero
```

このエラーを上から読むと 11 行目で “value = a.test(b)” を実行し、3行目で” return b.div(0)” を実行し、
7 行目で “return 5/value” を実行し、そこで ZeroDivisionError となったことが分かります。

## traceback モジュール

先ほど説明した「エラーを変数に格納し出力する」ことである程度の詳細を得ることは可能です。
ただ、より詳細を把握したい場合は traceback モジュールを使ってプログラムを停止することなくスタックトレースを取得すると便利です。
サンプルコードを以下に記載します。

```python
import traceback

print(1)
try:
  print(2)
  5/0
  print(3)
except Exception:
  print(4)
  # 文字列で取得
  text = traceback.format_exc()
  print(text)
  # ファイルに書き込み
  f = open('error.log', 'a')
  traceback.print_exc(file=f)
print(5)
```

上記では traceback モジュールの関数を2つ使っています。
ひとつめの format_exc() 関数はスタックトレースを文字列として返し、
2つめのprint_exc() は渡されたファイルオブジェクトにスタックトレースを書き込みます。
上記の実行結果は以下となります。

```
$ python3 test.py
1
2
4
Traceback (most recent call last):
  File "test.py", line 6, in <module>
    5/0
ZeroDivisionError: division by zero

5
```

また上記スタックトレースと同じ内容が書かれたファイルも作成されています。
プログラムの標準出力ではなくログファイルに出力する際にはこの機能を使うか、
もしくは logging モジュールを使ってエラーの文字列をファイルに書くのがよいと思います。
