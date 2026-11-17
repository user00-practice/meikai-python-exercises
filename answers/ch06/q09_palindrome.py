# 第6章　文字列　問9　解答例
s = input('文字列：')
if s == s[::-1]:
    print('回文です')
else:
    print('回文ではありません')
