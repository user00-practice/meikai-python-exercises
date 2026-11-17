# 第4章　プログラムの流れの繰返し　問9　解答例
total = 0
while True:
    x = int(input('整数：'))
    if x == 0:
        break
    total += x
print(f'合計は{total}です')
