TAX_RATE = 0.1


def with_tax(price):
    """税込価格（1円未満切り捨て）を返す"""
    return int(price * (1 + TAX_RATE))
