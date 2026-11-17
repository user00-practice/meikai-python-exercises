# 第11章　クラス　問10　解答例
import math


class Shape:
    def area(self):
        return 0

    def __str__(self):
        return f'{type(self).__name__}：面積 {self.area():.1f}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


shapes = [Square(3), Circle(2), Square(1.5)]
for s in shapes:
    print(s)
print(f'合計面積：{sum(s.area() for s in shapes):.1f}')
