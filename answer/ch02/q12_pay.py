# 第2章　画面への表示とキーボードからの入力　問12　解答例
wage = int(input('時給：'))
minutes = int(input('働いた時間(分)：'))
pay = wage * minutes // 60
print(f'給料は{pay:,}円です')
