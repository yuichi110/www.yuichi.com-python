# バイナリファイルの読み書き

{{ TOC }}

## 概要

あいうえお

### バイナリファイルをどのように処理するか

テキストファイルの主要な話を終えたため、次はバイナリファイルについて扱います。
バイナリファイルは中身が01から構成されているファイルで、一般的には画像ファイルや音声ファイル、
それに加えてアプリケーション特有のファイル(たとえば word など)があります。
こちらはテキストと違うのでそもそも行という概念がありません。
正直なことをいうと、テキスト処理よりもバイナリファイルの処理は骨が折れます。
ただ、ファイルを読み書きできないかというと、そんなことはありません。
そのバイナリファイルの構造を知ってさえいれば操作は可能です。

著者はビットマップ形式の画像ファイルの合成とWAV形式の音声データの加工の経験があるので、
それをベースにしてバイナリファイルの処理についてお話をします。

ビットマップは以下の図のように、ピクセルから構成されている画像ファイルです。

![image](./0090_image/04.jpg)

それぞれのピクセルはRGB(赤緑青)で表現されています。
それぞれの色は1バイト(0～255)の容量があるので、ようするに1ピクセルは3バイトです。
つまりファイルサイズは「縦のピクセル数×横のピクセル数×3」バイトになります。

ここまでわかってしまえば、あとは簡単です。たとえば画像Aに画像Bをオーバーレイ(一部上書き)するとします。
この際、Bの画像の黒(RGBが0, 0, 0)は透過させます。すると、以下の図のようにして合成が可能です。

![image](./0090_image/05.jpg)

Bの左上は黒なのでAのものを合成画像に利用。その右隣は黒ではないのでBのものを利用。
その右隣はA……といった感じでどんどん処理をしていくと、最終的に右の図のようになります。
これをファイルに書き込めば、自分でバイナリファイルを作ったことになります。

次にWAV音声ファイルです。これも比較的わかりやすい形式ですが、
先ほどのビットファイルと違って「ヘッダ」と「データ」に分かれています。
データは先程のビットマップと同じく音声のデータ(波形)を含んでいるだけなので簡単ですが、
ヘッダにはデータをどのように表現するかといった情報が含まれています。

![image](./0090_image/06.jpg)

後ろのデータを変えれば当然再生される音も変わりますが、その際に必要に応じてヘッダを変更する必要があります。

最後にバイナリデータの処理のコツを伝えます。
それは「プログラムで処理しやすい生(raw)の形式に一旦戻す」ということです。
たとえばビットマップであれば編集は簡単ですが、JPEGやPNGを編集するのは非常に難しいです。
なぜなら RAW 形式に比べて JPEG や PNG形式が画像をどのように表現するかがはるかに複雑だからです。
JPEG を直接操作するのであれば、JPEG に関する深い知識が必要になります。
その分野を専門としているプログラマ以外には実装することはできないでしょう。

まずJPEG → ビットマップに変換してやり、ビットマップで編集を行う。
そしてビットマップ → JPEGに再度変換することで JPEG ファイルを変換できます。
音声も同じでmp3を直接編集するのではなく、mp3 → wav → 編集 → new wav →new mp3とすればよいです。
これらの変換には組み込みもしくは外部のライブラリを利用することになると思います。
