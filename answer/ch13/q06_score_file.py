# 第13章　ファイル処理　問6　解答例
total = 0
count = 0
with open('score.txt', encoding='utf-8') as f:
    for line in f:
        name, score = line.rstrip().split(',')
        score = int(score)
        print(f'{name}：{score}点')
        total += score
        count += 1
print(f'人数 {count}　合計 {total}　平均 {total / count:.1f}')
