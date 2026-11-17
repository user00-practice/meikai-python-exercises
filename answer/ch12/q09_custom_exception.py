# 第12章　例外処理　問9　解答例
class InsufficientFundsError(Exception):
    """残高不足を表す例外"""
    pass


def withdraw(balance, amount):
    """引き出したあとの残高を返す"""
    if amount < 0:
        raise ValueError('金額が負です')
    if amount > balance:
        raise InsufficientFundsError(f'残高不足：あと{amount - balance}円')
    return balance - amount


balance = 1000
for amount in [300, 3000, -5, 200]:
    try:
        balance = withdraw(balance, amount)
        print(f'{amount}円引き出しました。残高 {balance}円')
    except InsufficientFundsError as e:
        print('エラー：', e)
    except ValueError as e:
        print('入力エラー：', e)
