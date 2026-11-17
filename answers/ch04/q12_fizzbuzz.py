# 第4章　プログラムの流れの繰返し　問12　解答例
n = int(input('いくつまで：'))
for i in range(1, n + 1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
