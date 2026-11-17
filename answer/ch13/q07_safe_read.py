# 第13章　ファイル処理　問7　解答例
name = input('ファイル名：')
try:
    with open(name, encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f'{name} が見つかりません')
else:
    print(f'{name} は {len(lines)} 行です')
