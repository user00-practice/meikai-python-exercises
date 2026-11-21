# 第9章　関数　問13　解答例
def grade(score: int) -> str:
    """点数から評価（A〜D）を返す"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'


scores = [int(x) for x in input('点数をスペース区切りで：').split()]
for s in scores:
    print(f'{s:3}点：{grade(s)}')
results = list(map(grade, scores))
print(f'A の人数：{results.count("A")}')
