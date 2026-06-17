# 导包
import requests
import config


class OrderAPI:
    # 1、登录
    def login(self, username, password):
        url = config.BASE_URL + "/wx/auth/login"
        login_data = {"username": username, "password": password}
        response = requests.post(url=url, json=login_data)
        return response

    # 2、搜索
    def search(self, keyword):
        return requests.get(url=config.BASE_URL + f"/wx/goods/list?keyword={keyword}&page=1&limit=10&categoryId=0")

    # 3、加入购物车
    def add_cart(self, token, add_data):
        return requests.post(url=config.BASE_URL + "/wx/cart/add", json=add_data, headers={"X-Litemall-Token": token})

    # 4、提交订单
    def submit_order(self, token, order_data):
        return requests.post(url=config.BASE_URL + "/wx/order/submit", json=order_data,
                             headers={"X-Litemall-Token": token})


if __name__ == '__main__':
    # 登录
    order_api = OrderAPI()
    response = order_api.login(username="user123", password="user123")
    # 提取token
    token = response.json().get("data").get("token")
    print(token)
    # 搜索
    response = order_api.search(keyword="母亲节")
    goods_id = response.json().get("data").get("list")[0].get("id")
    print(goods_id)
    # 添加购物车
    add_data = {"goodsId": goods_id, "number": 5, "productId": 2}
    response = order_api.add_cart(token, add_data)
    print(response.json())
    # 提交订单
    test_data = {"addressId": "19", "cartId": "0", "couponId": "0", "userCouponId": "0", "grouponLinkId": 0,
                 "grouponRulesId": 0, "message": ""}
    response = order_api.submit_order(token=token, order_data=test_data)
    print(response.json())
