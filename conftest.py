import pytest
import yaml

from pythoncode.caculator import Calculator


def get_datas():
    with open("./data.yml", 'rb') as f:
        datas = yaml.safe_load(f)

        return datas


@pytest.fixture(scope='module',autouse=True)
def add_fixture():
    print('执行之前进行steup操作')
    yield
    print('执行之后进行teardown操作')

