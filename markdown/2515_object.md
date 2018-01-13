## 関数オブジェクト

先程もお伝えしましたがPython は関数自体もオブジェクトです。
そのため、変数に関数を代入し、それを利用することができます。

```python
def test1():
  print('test1')

a = test1
a()
# test1
```

変数に代入できるということは関数の引数として使えるということです。
詳細は中編にて取り扱いますが、関数を使う関数である高階関数というものもあります。

```python
def apply_list(fun, list_):
  for i in list_:
    fun(i)

def print_double(x):
  print(x * 2)

list_ = [1,2,3,4,5]
apply_list(print_double, list_)
# 2
# 4
# 6
# 8
# 10
```
