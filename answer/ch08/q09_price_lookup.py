# 第8章　タプルと辞書と集合　問9　解答例
PRICES = {'りんご': 100, 'みかん': 80, 'ぶどう': 300}
name = input('品名：')
if name in PRICES:
    print(f'{name}は{PRICES[name]}円です')
else:
    print(f'{name}は扱っていません')
