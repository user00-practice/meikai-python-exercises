# 第9章　関数　問12　解答例
def is_prime(n: int) -> bool:
    """n が素数なら True を返す"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('いくつまで：'))
primes = [x for x in range(2, n + 1) if is_prime(x)]
print(*primes)
