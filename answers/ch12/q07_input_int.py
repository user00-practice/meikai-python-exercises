# 第12章　例外処理　問7　解答例
while True:
    try:
        n = int(input('整数：'))
        break
    except ValueError:
        print('整数を入力してください')
print(f'{n} の2倍は {n * 2} です')
