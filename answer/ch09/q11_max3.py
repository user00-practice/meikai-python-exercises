# 第9章　関数　問11　解答例
def max3(a, b, c):
    """a・b・c の最大値を返す"""
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


x = int(input('a：'))
y = int(input('b：'))
z = int(input('c：'))
print(f'最大値は{max3(x, y, z)}です')
