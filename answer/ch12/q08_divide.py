# 第12章　例外処理　問8　解答例
try:
    a = int(input('割られる数：'))
    b = int(input('割る数：'))
    q = a / b
except ValueError:
    print('整数を入力してください')
except ZeroDivisionError:
    print('0 では割れません')
else:
    print(f'{a} ÷ {b} = {q:.2f}')
finally:
    print('計算を終わります')
