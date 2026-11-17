# 第10章　モジュールとパッケージ　問6　解答例
from shop.cart import total

items = [int(x) for x in input('価格をスペース区切りで：').split()]
print(f'税込合計：{total(items):,}円')
