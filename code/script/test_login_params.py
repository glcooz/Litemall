# 导包
from api.order import OrderAPI
from commom.utils import *
import pytest
import config


# Fixture
@pytest.fixture(scope="function")
def login_fixture():
    print("开始执行登录测试")
    yield
    print("登录测试执行结束")


# 创建测试类
class TestLoginAPI:
    # 类前置处理
    def setup_class(self):
        # 实例化
        self.order_api = OrderAPI()

    # 登录
    @pytest.mark.parametrize("username, pwd, status, code, msg", read_json_file(config.BASE_PATH + "/data/login.json"))
    def test_login(self, username, pwd, status, code, msg, login_fixture):
        response = self.order_api.login(username=username, password=pwd)
        print(response.json())
        common_assert(response, status, code, msg)
