from .price import with_tax


def total(items):
    """価格のリストの税込合計を返す"""
    return sum([with_tax(p) for p in items])
