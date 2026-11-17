# 第11章　クラス　問8　解答例
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f'長方形（横{self.width}×縦{self.height}）'


r = Rectangle(5, 3)
print(r)
print(f'面積：{r.area()}　周の長さ：{r.perimeter()}')
