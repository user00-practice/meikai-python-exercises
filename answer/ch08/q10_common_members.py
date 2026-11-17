# 第8章　タプルと辞書と集合　問10　解答例
a = set(input('Aの参加者：').split())
b = set(input('Bの参加者：').split())
print(f'両方：{sorted(a & b)}')
print(f'どちらか：{sorted(a | b)}')
print(f'Aだけ：{sorted(a - b)}')
