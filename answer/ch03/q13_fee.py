# 第3章　プログラムの流れの分岐　問13　解答例
age = int(input('年齢：'))
if age < 6:
    fee = 0
elif age >= 65:
    fee = 500
else:
    fee = 1000
print(f'入場料は{fee}円です')
