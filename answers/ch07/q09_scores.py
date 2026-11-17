# 第7章　リスト　問9　解答例
scores = []
while True:
    s = input('点数：')
    if s == '':
        break
    scores.append(int(s))
print(f'人数 {len(scores)}　合計 {sum(scores)}　平均 {sum(scores) / len(scores):.1f}')
print(f'最高 {max(scores)}　最低 {min(scores)}')
