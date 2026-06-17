# 导包
from api.order import OrderAPI
from commom.utils import common_assert


# 创建测试类
class TestLoginAPI:
    # 类前置处理
    def setup_class(self):
        # 实例化
        self.order_api = OrderAPI()

    # 登录成功
    def test_login_success(self):
        # 调用登录接口
        # 实例化接口类.接口方法(接口参数数据)
        response = self.order_api.login(username="user123", password="user123")
        print(response.json())
        common_assert(response)

    # 登录失败（账号为空）
    def test_login_fail_username_empty(self):
        response = self.order_api.login(username="", password="user123")
        print(response.json())
        common_assert(response, 200, 700, "不存在")

    # 登录失败（账号不存在）
    def test_login_fail_username_not_exist(self):
        response = self.order_api.login(username="user45678", password="user123")
        print(response.json())
        common_assert(response, 200, 700, "不存在")

    # 登录失败（密码为空）
    def test_login_fail_password_empty(self):
        response = self.order_api.login(username="user123", password="")
        print(response.json())
        common_assert(response, 200, 700, "不对")

    # 登录失败（密码错误）
    def test_login_fail_password_error(self):
        response = self.order_api.login(username="user123", password="123456")
        print(response.json())
        common_assert(response, 200, 700, "不对")