# 文字列型

{{ TOC }}

## 概要

文字列はPythonでテキストデータを扱うための型です。
リストと同じシーケンス型に属していますので、ループやスライスといったテクニックが使えます。

文字列の宣言や結合といった単純な利用法は簡単です。
ただ、メソッドを使った様々な処理の一部は複雑なものです。
それらを理解するうえで重要なのは「文字列型は不変オブジェクト」ということをきちんと認識することです。
文字列を操作して変更する場合はインスタンス自体が変わるのではなく、
変更が加えられた新しいインスタンスが作成されて返されます。


## 文字列型の特徴

プログラミング言語ではテキスト処理を多用します。
文字列型はそのための型であるため、きちんと理解する必要があります。

「文字列」という名前からわかるように文字列型は「1文字」の「列」としても扱われます。
リストと同じように前から何番目というかたちで一部を抜き出したりすることができますし、
更新(正確にいうと新しく作成しなおす)することもできます。
これは文字列型がシーケンス型であるためです。

文字列が持つメソッドの数は他の基本的な型に比べるとかなり多いです。
全てを暗記することは難しいですが、どのようなものがあるかを曖昧にでも覚えておくと必要に応じて使えるようになります。


## 文字列の基本操作

### 文字列の宣言

文字列はシングルクオートで囲むことで宣言できます。

```text
>>> a = 'hello world'
>>> print(a)
hello world
>>> print(type(a))
<class 'str'>
```

シングルクオートの代わりにダブルクオートを使うこともできますが、
Pythonではシングルクオートの利用が標準的です。

```text
>>> a = "hello world"
>>> print(a)
hello world
>>> print(type(a))
<class 'str'>
```

シングルクオートとダブルクオートで作成された文字列に違いはありませんので、
特に理由がないかぎりはシングルクオートを利用します。

シングルクオートとダブルクオートを使い分ける場面は、
文字列内にシングルクオートかダブルクオートが文字として出現する場合です。
シングルクオートの文字列宣言のなかではダブルクオートを利用することができ、
その逆にダブルクオートの文字列宣言のなかでシングルクオートを使うことができます。

たとえば「I'm Taro」というテキストを文字列にする場合、
シングルクオートで文字列を宣言するのであれば内部のシングルクオートをエスケープ処理する必要があります。
これは文字列内にシングルクオートが文字として含まれているため、それを文字列を作る特別な記号としてではなく、
文字としてPythonに認識させる必要があるためです。

```text
>>> a = 'I\'m Taro'
>>> print(a)
I'm Taro
```

一方、ダブルクオートで囲むのであれば、その中にあるシングルクオートは文字として扱われるためエスケープは不要です。

```text
>>> a = "I'm Taro"
>>> print(a)
I'm Taro
```


### 複数行にまたがる文字列の宣言

複数行にまたがる文字列の宣言にはトリプルクオテーションを使います。
トリプルクオテーションはシングルクオテーションを3つか、ダブルクオテーション3つを続けることで宣言でき、
文字列の前後のトリプルクオテーションの記号は統一する必要があります。

```python
text = """line1
line2"""
print(text)
```

トリプルクオテーションの中ではトリプルクオテーションと同じ記号が3つ続かない限り、
シングルクオテーションとダブルクオテーションのどちらでも使えます。
そのため、文字列の中でシングルクオテーションやダブルクオテーションを複雑に使いたい場合は、
1行であってもトリプルクオテーションを使ってもよいかもしれません。

```python
text = '''I'm Taro. "Hello World"'''
print(text)
```

なお、Pythonでは複数行にまたがるコメント記法が正式には存在していません。
そのため、プログラムをトリプルクオテーションで文字列化してしまうことで実行しても影響をなくすようにします。
実質的にトリプルクオテーションが複数行のコメントに使われています。


### +演算子

+演算子を使うことで2つの文字列を結合できます。
もとの2つの文字列には変化はありません。

```text
>>> a = 'hello'
>>> b = ' world'
>>> print(a + b)
hello world
>>> print(a)
hello
>>> print(b)
 world
```

複合代入演算子を使うことで既存の文字列の後ろに新しい文字列を加えることもできます。

```text
>>> a = 'hello'
>>> a += ' world'
>>> print(a)
hello world
```

これは「a = a + ' world'」として処理されていますので、変数aのなかにある文字列自体が置き換えられています。
「最初に変数aに入っていた文字列のインスタンス」と、
実行後に変数aに代入されている「複合代入演算子で文字列が付け加えられた文字列のインスタンス」はメモリ上では別物になっています。
これは他の型の複合代入演算子の動きでも同じです。


### \*演算子

\*演算子を使うことで、文字列を指定した回数繰り返すことができます。

```text
>>> a = 'python'
>>> print(a * 3)
pythonpythonpython
```

複合代入演算子も使えます。

```text
>>> a = 'python'
>>> a *= 3
>>> print(a)
pythonpythonpython
```


### in演算子

in演算子を使うことである文字列のなかに指定した文字列があるか判定できます。
「含まれる文字列 in 含む文字列」とすると、文字列が含まれていればTrueが返り、
含まれていなければFalseが返ります。

```text
>>> text = 'hello python'
>>> print('pyt' in text)
True
>>> print('PYT' in text)
False
```

アルファベッドの大文字小文字は区別されます。
文字列のin演算は厳密に合致するかの判定をしますが、
あるパターンに合致するかを調べるのであれば正規表現を使います。


### 文字列長の取得

文字列型はリストと同じシーケンス型に分類されます。
そのため、len関数で長さ(文字列長)を得ることができます。

```text
>>> length = len('hello world')
>>> print(length)
11
```

日本語などのマルチバイト文字もきちんと1文字で1つカウントされます。

```text
>>> length = len('こんにちは')
>>> print(length)
5
```

### 文字列へのキャスト

print関数で出力する内容を作る場合などに、文字列型の値とその他の値を結合させることがあります。
たとえば計算結果の100をprint関数で「result: 100」と表示するなどです。

この場合、文字列の「'result: '」と数値の「100」を直接結合するとエラーになります。

```text
>>> a = 'result: ' + 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

エラーにあるように文字列に結合される値は文字列である必要があります。

このような場合は文字列以外の値を文字列にstr関数を使ってキャストします。

```text
>>> a = 'result: ' + str(100)
>>> print(a)
result: 100
```

なお、文字列とそれ以外の型の値を結合したい場合は、
文字列型のformatメソッドを使うという方法もあります。


### for文で1文字単位でループ

文字列はシーケンス型なので、for文で使うことができます。
リストで要素単位でループを回すように、文字列は1文字単位でループを回します。

```python
text = 'hello'
for c in text:
  print(c)
```

```text
h
e
l
l
o
```


### 文字列内の文字の取得

文字列はリストと同じように「先頭から何番目」と指定することで、文字を抜き出すことができます。
指定方法は大カッコのなかにインデックス番号を書くというものです。

```text
>>> text = 'hello'
>>> print(text[0])
h
>>> print(text[3])
l
>>> print(text[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

範囲外へのアクセスはエラーとなります。


### 範囲を指定して文字列内の文字列を抜き出し

リストのスライスと同じようにして、
文字列内から「ここからここまで」と指定して文字列を抜き出すことができます。
「抜き出すもとの文字列[始まり:終わり]」とすると、
もとの文字列の始まりのインデックスから終わりのインデックスまでを抜き出して返します。


文字列から「文字列」を取得するには、以下のように行います。

```python
>>> text = 'hello python'
>>> print(text[3:8])
lo py
```

指定部分の前後を省略すると、それぞれ「文字列の最初から(0指定と同じ)」
「文字列の最後まで(最大のインデックス値と同じ)」という意味になります。
両方を省略すれば最初から最後までという意味になるので、完全に文字列がコピーされます。

```python
>>> text = 'hello python'
>>> print(text[:8])
hello py
>>> print(text[3:])
lo python
>>> print(text[:])
hello python
```

リストと文字列は似ていますが、インスタンス自体が変化することはないので、
「del演算子(インスタンス内の要素を削除)」は使えません。
文字列から

## 文字列のエスケープ

```
\\	バックスラッシュ (\)	 
\'	一重引用符 (')	 
\"	二重引用符 (")	 
\a	ASCII 端末ベル (BEL)	 
\b	ASCII バックスペース (BS)	 
\f	ASCII フォームフィード (FF)	 
\n	ASCII 行送り (LF)	 
\r	ASCII 復帰 (CR)	 
\t	ASCII 水平タブ (TAB)	 
\v	ASCII 垂直タブ (VT)
```

## 文字列型の関数

### chr : ユニコードのコードポイントに対応する文字を取得


### ord : 文字のユニコードのコードポイントを取得


## 文字列型のメソッド

### replace : 文字列の部分置き換えと削除

replaceメソッドは呼び出し元の文字列にある第一引数の文字列を第二引数の文字列に置き換えた文字列を作成します。
たとえば「text.replace('o', '0')」とすればtextという変数に含まれる文字列'o'を'0'に置き換えた文字列を返します。
第一引数に合致する文字列が呼び出し元に複数あった場合、それは全て置き換えられます。

```text
>>> text = 'hello world python'
>>> a = text.replace('o', '0')
>>> print(a)
hell0 w0rld pyth0n
>>> print(text)
hello world python
```

文字列のメソッドを呼び出しても、呼び出し元のインスタンスに変化はおきません。
返り値として新しい文字列を作るのであり、呼び出し元の文字列に手を加えるわけではないことは注意をしてください。

置き換える文字列を空文字「''」とすれば、置き換えられる文字が消された文字列が返されます。

```text
>>> text = 'hello world python'
>>> a = text.replace('ll', '')
>>> print(a)
heo world python
```


### find : 引数の文字列と合致したインデックスの取得

文字列のfindメソッドはin演算子に似ています。
インスタンスの文字列内に、引数で与えた文字列が含まれていればインデックス番号を返します。
含まれていなければ「-1」を返します。

```text
>>> text = 'hello python'
>>> a = text.find('llo')
>>> print(a)
2

>>> b = text.find('PYTHON')
>>> print(b)
-1
```

返り値が-1か否かで、文字列中の特定文字列の存在の確認をできます。
ただ、オプションなどを必要としないのであればin演算子を使うほうが明確です。
同じ文字列が複数含まれていれば、一番最初に合致したインデックス番号を返します。

このメソッドにはオプションの引数があり、文字列のどこからどこまでをチェックするかを指定できます。
第二引数(start)が開始位置で第三引数(end)が検索対象の終了位置です。

```text
>>> text = 'hello python'
>>> a = text.find('llo', 5)
>>> print(a)
-1
```

上記のサンプルでは検索対象が5文字め以降になっているため、
'llo'が文字列に含まれているにも関わらず、
返り値が-1(含まれていなかった)となっています。


### rfind : findを文字列末尾から実施

findは文字列の先頭側から合致した箇所を探します。
rfindはこの逆で、文字列の末尾側から合致した箇所を探します。

```text
>>> text = '01234567890123456789'
>>> text.find('9')
9
>>> text.rfind('9')
19
```


### index : findメソッドとほぼ同じ

文字列のindexメソッドは文字列のfindメソッドとほとんど同じです。
findメソッドが文字列が見つからなかった場合にインデックス位置を-1として返すのに対し、
indexメソッドでは例外を発生させます。

```text
>>> text = 'hello python'
>>> a = text.index('llo')
>>> print(a)
2
```

文字列中に指定した文字列が存在しない場合は「ValueError」が発生します。

```text
>>> b = text.index('PYTHON')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```


### rindex : indexメソッドを文字列末尾から実施

rindexメソッドはindexメソッドの文字列末尾から検索する版です。
findとrfindの関係と全く同じです。

```text
>>> text = '01234567890123456789'
>>> text.rindex('9')
19

>>> text.rindex('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```


### startswith : 文字列が特定文字列から始まるか

startswithメソッドは文字列が引数でした文字列から始まるかを判定します。
引数で与えた文字列から始まればTrueが返され、そうでなければFalseが返ります。
in演算子での判定ををより限定的にしたようなものです。

```text
>>> text = 'hello python'
>>> a = text.startswith('hello')
>>> print(a)
True

>>> b = text.startswith('python')
>>> print(b)
False
```


### endswith : 文字列が特定文字列で終わるか

endswithメソッドは文字列が引数でした文字列で終わるかを判定します。
引数で与えた文字列から始まればTrueが返され、そうでなければFalseが返ります。
startswithメソッドと似ています。

```text
>>> text = 'hello python'
>>> a = text.endswith('hello')
>>> print(a)
False

>>> b = text.endswith('python')
>>> print(b)
True
```


### strip : 文字列の前後の削除

stripメソッドを使うことで文字列の前後にある特定文字列(第一引数で指定)を省くことができます。
メソッド呼び出し元の文字列の前後に省かれる文字列がなければ、省かれずに無視されるだけです。

第一引数を省略した場合はデフォルトの「空白文字列(スペースだけでなくタブや改行も含む)」を省きます。

```text
>>> text = ' hello world \n'
>>> a = text.strip()
>>> print(a)
hello world
>>>
```

上記では先頭の空白と最後の空白及び改行コードが削られています。

第一引数を指定した場合はそれを削ります。
同じパターンが続く限りは何度でもそれを削ります。

```text
>>> text = '123123456123'
>>> a = text.strip('123')
>>> print(a)
456
```


### lstrip : 文字列の前部の削除

stripメソッドは文字列の前後から特定文字列を削ります。
lstripメソッドは「left」の「l」がついているように、左側(つまり前部)のみを削ります。

引数を省略した場合のデフォルトはstripと同じく空白文字の削除です。

```python
>>> text = ' hello world \n'
>>> a = text.lstrip()
>>> print(a)
hello world

>>>
```

上記の結果では、前部の空白は削られているのに対して後部の改行はそのまま残っています。

第一引数で文字列をしても前部のみを削ります。

```text
>>> text = '123123456123'
>>> a = text.lstrip('123')
>>> print(a)
456123
```


### rstrip : 文字列の後部の削除

rstripは「right strip」ですので、文字列の右側(後部)のみ削ります。

引数を省略した場合のデフォルトはstripやlstripと同じく空白文字の削除です。

```text
>>> a = text.rstrip()
>>> print(a)
 hello world
>>>
```

前部の空白が残っているのに対し、後者の改行文字及び空白が削除されています。

第一引数で文字列をしても後部のみを削ります。

```text
>>> text = '123123456123'
>>> a = text.rstrip('123')
>>> print(a)
123123456
```


### split : 文字列の分割

splitメソッドを使うことで文字列を第一引数で指定した区切り文字で分割できます。
分割された文字列はリストに前から順につめられて返されます。

```text
>>> text = '1, taro, 35, male'
>>> a = text.split(',')
>>> print(a)
['1', ' taro', ' 35', ' male']
```

上記ではCSV形式で使われるコンマ区切りのデータをコンマで区切ってリストにまとめています。
今回であれば返り値であるリストの各要素にたいしてstripメソッドを適用して空白を削除してもよいかもしれません。

区切り文字が2つ以上連続で続く場合は、そのあいだの要素は空文字になります。

```text
>>> text = '1, taro,, male'
>>> a = text.split(',')
>>> print(a)
['1', ' taro', '', ' male']
```


### splitlines : 文字列を改行コードで分割

splitlinesメソッドは文字列を改行コード系で区切ります。
改行コードだけでなく改ページなどのコードでも区切られますので、splitメソッドに「'\\n'」を与えた場合と厳密には違った動きをします。

```text
>>> text = '1\ntaro\n35\nmale'
>>> a = text.splitlines()
>>> print(a)
['1', 'taro', '35', 'male']
```


### join : 文字列でリストを連結

joinメソッドは呼び出し元の文字列で引数のリストを1つの文字列に連結します。
splitメソッドの反対です。

```text
>>> text = ' ,'
>>> a = text.join(['1', 'taro', '35', 'male'])
>>> print(a)
1 ,taro ,35 ,male
```

連結されるリスト内の要素は文字列である必要があります。
たとえば、上記の'35'が数値の35であればエラーになります。

```text
>>> text = ' ,'
>>> a = text.join(['1', 'taro', 35, 'male'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 2: expected str instance, int found
```


### lower : アルファベットを小文字にする

lowerメソッドを呼び出すことで、文字列のアルファベットを全て小文字にできます。

```text
>>> text = 'HeLlO wOrLd'
>>> a = text.lower()
>>> print(a)
hello world
```

アルファベット以外の文字が含まれていてもエラーにはならず、無視されます。

```text
>>> text = '123 ABC 456 あいうえお'
>>> a = text.lower()
>>> print(a)
123 abc 456 あいうえお
```

### upper : アルファベットを大文字にする

upperメソッドを呼び出すことで、文字列のアルファベットを全て小文字にできます。

```text
>>> text = 'HeLlO wOrLd'
>>> a = text.upper()
>>> print(a)
HELLO WORLD
```

### title : 区切り文字を大文字にする

英文などでは単語の区切り文字のみを大文字にすることがよくあります。
titleメソッドを呼び出すことで、文字列の単語の頭だけを大文字にできます。

```text
>>> text = 'HeLlO wOrLd'
>>> a = text.title()
>>> print(a)
Hello World
```

### zfill : 数値の左に0をつめる

zfillメソッドを使うことで、数字を持つ文字列の先頭に0をつめることができます。
引数で指定した文字列長になるように0をつめます。

```text
>>> text = '123'
>>> a = text.zfill(5)
>>> print(a)
00123
>>> a = text.zfill(6)
>>> print(a)
000123
```

使う用途はあまりないと思いますが、数字以外に対しても0をつめることができます。

```text
>>> text = 'ABC あいうえお'
>>> a = text.zfill(15)
>>> print(a)
000000ABC あいうえお
```

### isalnum

isalnumメソッドは文字列が空でなく、数値とアルファベットのみから構成されているかを調べます。
条件を満たしていればTrueが返り、そうでなければFalseが返ります。

```text
>>> text = '012345abcDE'
>>> print(text.isalnum())
True
>>> text = '012345 abcDE'
>>> print(text.isalnum())
False
```

### isalpha

isalphaメソッドは文字列が空でなく、アルファベットのみから構成されているかを調べます。
条件を満たしていればTrueが返り、そうでなければFalseが返ります。

```text
>>> text = 'abcdeFGHIJ'
>>> print(text.isalpha())
True
>>> text = 'abcDE12345'
>>> print(text.isalpha())
False
```

### isdigit

isdeigtメソッドは文字列が空でなく、数値のみから構成されているかを調べます。
ここでいう数値は「0123456789」のことであり、小数点「.」や16進数の「ABCDEF」は含みません。
条件を満たしていればTrueが返り、そうでなければFalseが返ります。

```text
>>> text = '0123456789'
>>> print(text.isdigit())
True
>>> text = '012345.6789'
>>> print(text.isdigit())
False
```

### islower

islowerメソッドは文字列が小文字であるかを調べます。
条件を満たしていればTrueが返り、そうでなければFalseが返ります。

```text
>>> text = 'abcde'
>>> print(text.islower())
True
>>> text = 'abcdeFGHIJ'
>>> print(text.islower())
False
```

正確に言えば「1文字以上の小文字があるか」「大文字はひとつもないか」を調べるので、
空白や数値、日本語といったアルファベットと異なる文字は無視します。

```text
>>> text = 'abcde12345'
>>> print(text.islower())
True
```

### isupper

islowerメソッドは文字列が大文字であるか(「1文字以上の大文字があるか」「小文字はひとつもないか」)を調べます。
条件を満たしていればTrueが返り、そうでなければFalseが返ります。

```text
>>> text = 'ABCDE'
>>> print(text.isupper())
True

>>> text = 'ABCDEfghij'
>>> print(text.isupper())
False

>>> text = 'ABCDE12345'
>>> print(text.isupper())
True
```

### istitle

```text
>>> text = 'Hello World'
>>> print(text.istitle())
True

>>> text = 'hello world'
>>> print(text.istitle())
False

>>> text = 'Hello 12345 World'
>>> print(text.istitle())
True
```
