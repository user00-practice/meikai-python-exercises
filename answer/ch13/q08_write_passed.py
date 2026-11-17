# 第13章　ファイル処理　問8　解答例
PASS_LINE = 70

passed = []
with open('score.txt', encoding='utf-8') as f:
    for line in f:
        name, score = line.rstrip().split(',')
        if int(score) >= PASS_LINE:
            passed.append(name)

with open('passed.txt', 'w', encoding='utf-8') as f:
    for i, name in enumerate(passed, 1):
        print(f'{i}. {name}', file=f)

with open('passed.txt', encoding='utf-8') as f:
    print(f.read(), end='')
