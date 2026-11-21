# 第3章　プログラムの流れの分岐　問14　解答例
m = int(input('月：'))
match m:
    case 12 | 1 | 2:
        print('冬です')
    case 3 | 4 | 5:
        print('春です')
    case 6 | 7 | 8:
        print('夏です')
    case 9 | 10 | 11:
        print('秋です')
    case _:
        print('1〜12で入力してください')
