from decimal import Decimal


class Calculator:
    def add(self, a, b):
        if isinstance(a or b, str):
            return "请输入数字"
        else:
            return a + b

    def sub(self, a, b):
        if isinstance(a or b, str):
            return "请输入数字"
        elif isinstance(a or b, float):
            return float(Decimal(a - b).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP"))
        else:
            return a - b

    def mul(self, a, b):
        if isinstance(a or b, str):
            return "请输入数字"
        elif isinstance(a or b , float):
            return float(a * b)
        else:
            return a * b

    def div(self, a, b):
        if isinstance(a or b, str):
            return "请输入数字"
        elif isinstance(a or b, float):
            return float(Decimal(a / b).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP"))
        elif b == 0:
            return '除数不能为0'
        else:
            return a / b
