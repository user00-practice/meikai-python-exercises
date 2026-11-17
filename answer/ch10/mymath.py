"""簡単な計算のモジュール"""


def square(x):
    """x の2乗を返す"""
    return x * x


def is_even(n):
    """n が偶数なら True を返す"""
    return n % 2 == 0


if __name__ == '__main__':
    print(square(3), is_even(4))
