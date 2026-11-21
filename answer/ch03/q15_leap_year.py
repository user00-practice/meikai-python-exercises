# 第3章　プログラムの流れの分岐　問15　解答例
year = int(input('西暦：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('うるう年です')
else:
    print('うるう年ではありません')
