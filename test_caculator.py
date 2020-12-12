import pytest

from pythoncode.caculator import Calculator


class Test_caculator:
    def setup_class(self):
        self.caculator = Calculator()
        print("用例开始执行")

    def teardown_class(self):
        print("用例结束执行")

    @pytest.mark.parametrize("a,b,res",
                             [(0, 0, 0), (1, 2, 3), (-1, -2, -3), (1.2, 1.3, 2.5), (-1.2, -1.3, -2.5),
                              ("one", "two", "请输入数字")],
                             ids=["zero", "positive", "negative", "decimal", "negative_decimal", "str"])
    def test_add(self, a, b, res):
        assert self.caculator.add(a, b) == res

    @pytest.mark.parametrize("a,b,res",
                             [(0, 0, 0), (3, 2, 1), (-1, -2, 1), (1.3, 1.2, 0.1), (-1.3, -1.2, -0.1)
                              , ("one", "two", "请输入数字")],
                             ids=["zero", "positive", "negative", "decimal", "negative_decimal",  "str"])
    def test_sub(self, a, b, res):
        assert self.caculator.sub(a, b) == res

    @pytest.mark.parametrize("a,b,res",
                             [(0, 0, 0), (3, 2, 6), (-1, -2, 2), (1.3, 1.2, 1.56), (-1.3, -1.2, 1.56)
                                 , ("one", "two", "请输入数字")],
                             ids=["zero", "positive", "negative", "decimal", "negative_decimal", "str"])
    def test_mul(self, a, b, res):
        assert self.caculator.mul(a, b) == res

    @pytest.mark.parametrize("a,b,res",
                             [(0, 0, "除数不能为0"), (3, 2, 1.5), (-1, -2, 0.5), (1.3, 1.2, 1.1), (-1.3, -1.2, 1.1)
                                 , ("one", "two", "请输入数字")],
                             ids=["zero", "positive", "negative", "decimal", "negative_decimal", "str"])
    def test_div(self, a, b, res):
        assert self.caculator.div(a, b) == res
