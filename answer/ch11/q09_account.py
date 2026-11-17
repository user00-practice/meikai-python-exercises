# 第11章　クラス　問9　解答例
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('金額が正しくありません')
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('残高不足です')
            return
        self.__balance -= amount

    def __str__(self):
        return f'{self.name}：{self.__balance:,}円'


a = Account('佐藤', 1000)
a.deposit(500)
a.withdraw(3000)
a.withdraw(200)
print(a)
print(a.balance)
