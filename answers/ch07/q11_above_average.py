# 第7章　リスト　問11　解答例
scores = [int(x) for x in input('点数をスペース区切りで：').split()]
avg = sum(scores) / len(scores)
above = [s for s in scores if s >= avg]
print(f'平均：{avg:.1f}')
print(f'平均以上：{above}')
