# 第6章　文字列　問11　解答例
s = input('文字列：')
alpha = 0
digit = 0
other = 0
for c in s:
    if c.isalpha():
        alpha += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print(f'英字：{alpha}　数字：{digit}　その他：{other}')
