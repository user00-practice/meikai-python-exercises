# 第2章　画面への表示とキーボードからの入力　問11　解答例
height = float(input('身長(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'BMIは{bmi:.1f}です')
