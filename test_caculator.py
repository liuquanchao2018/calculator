import pytest
import yaml



from pythoncode.caculator import Calculator


def get_datas():
    with open("./data.yml",'rb') as f:
        datas = yaml.safe_load(f)
        return datas
@pytest.fixture(params=get_datas()['add']['data'])
def aaa(request):
    return request.param

class Test_caculator:
    def setup_class(self):
        self.caculator = Calculator()
        print("用例开始执行")

    def teardown_class(self):
        print("用例结束执行")


    @pytest.mark.parametrize("a,b,res",get_datas()['add']['data'],ids= get_datas()['add']['ids']

                             )
    @pytest.mark.run(order=2)
    def test_add(self, a, b, res):
        assert self.caculator.add(a, b) == res

    @pytest.mark.parametrize("a,b,res", get_datas()['sub']['data'],ids= get_datas()['sub']['ids']
                             )
    @pytest.mark.run(order=1)
    def test_sub(self, a, b, res):
        assert self.caculator.sub(a, b) == res

    @pytest.mark.parametrize("a,b,res", get_datas()['mul']['data'],ids= get_datas()['mul']['ids']
                             )
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, res):
        assert self.caculator.mul(a, b) == res

    @pytest.mark.parametrize("a,b,res", get_datas()['div']['data'],ids= get_datas()['div']['ids']
                             )
    @pytest.mark.run(order=4)
    def test_div(self, a, b, res):
        assert self.caculator.div(a, b) == res
