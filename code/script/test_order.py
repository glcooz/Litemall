# 导包
from api.order import OrderAPI
from commom.utils import *


# 创建测试类
class TestOrderAPI:
    # 初始化属性
    token = None
    goods_id = None

    # 类前置方法
    def setup_class(self):
        # 实例化接口类
        self.order_api = OrderAPI()

    # 登录
    def test_login(self):
        response = self.order_api.login(username="user123", password="user123")
        # 提取token
        TestOrderAPI.token = response.json().get("data").get("token")
        # print(TestOrderAPI.token)
        # # 断言响应状态码为200
        # assert response.status_code == 200
        # # 断言响应数据中errno值为0
        # assert response.json().get("errno") == 0
        # # 断言响应数据中errmsg值为成功
        # assert "成功" in response.text
        common_assert(response)


    # 搜索
    def test_search(self):
        response = self.order_api.search(keyword="母亲节")
        TestOrderAPI.goods_id = response.json().get("data").get("list")[0].get("id")
        print(TestOrderAPI.goods_id)
        # # 断言响应状态码为200
        # assert response.status_code == 200
        # # 断言响应数据中errno值为0
        # assert response.json().get("errno") == 0
        # # 断言响应数据中errmsg值为成功
        # assert "成功" in response.text
        common_assert(response)

    # 添加购物车
    def test_add_cart(self):
        add_data = {"goodsId": TestOrderAPI.goods_id, "number": 5, "productId": 2}
        response = self.order_api.add_cart(TestOrderAPI.token, add_data)
        print(response.json())
        # # 断言响应状态码为200
        # assert response.status_code == 200
        # # 断言响应数据中errno值为0
        # assert response.json().get("errno") == 0
        # # 断言响应数据中errmsg值为成功
        # assert "成功" in response.text
        common_assert(response)

    # 提交订单
    def test_submit_order(self):
        test_data = {"addressId": "19", "cartId": "0", "couponId": "0", "userCouponId": "0", "grouponLinkId": 0,
                     "grouponRulesId": 0, "message": ""}
        response = self.order_api.submit_order(token=TestOrderAPI.token, order_data=test_data)
        print(response.json())
        # # 断言响应状态码为200
        # assert response.status_code == 200
        # # 断言响应数据中errno值为0
        # assert response.json().get("errno") == 0
        # # 断言响应数据中errmsg值为成功
        # assert "成功" in response.text
        # 查看实际的 errno 值
        # print(f"errno: {response.json().get('errno')}")
        # print(f"errmsg: {response.json().get('errmsg')}")
        common_assert(response)

