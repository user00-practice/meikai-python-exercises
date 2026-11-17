# 第4章　プログラムの流れの繰返し　問11　解答例
n = int(input('段数：'))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
