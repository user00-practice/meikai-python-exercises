# 第8章　タプルと辞書と集合　問8　解答例
text = input('単語をスペース区切りで：')
count = {}
for w in text.split():
    count[w] = count.get(w, 0) + 1
for w, c in count.items():
    print(f'{w}：{c}回')
