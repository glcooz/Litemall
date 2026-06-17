# 轻商城 (Litemall) 接口自动化测试项目
本项目是基于**Pytest**框架的轻商城（Litemall）商城系统接口自动化测试套件，覆盖了首页、注册、登录、搜索、购物车、订单、地址管理、收藏等核心业务场景。

## 项目结构
.
├── code/
│ ├── api/ # 接口封装层（各业务模块的请求方法）
│ ├── common/ # 公共工具类（数据库连接、通用函数等）
│ ├── data/ # 测试数据（如登录账号、商品ID等）
│ ├── script/ # 测试用例（按功能模块划分）
│ ├── config.py # 项目配置文件（域名、数据库、登录账号等）
│ └── pytest.ini # Pytest 配置文件
├── report/ # 测试报告输出目录（自动生成）
├── .gitignore # Git 忽略文件配置
├── README.md # 项目说明
├── 轻商城-API文档.md # 接口文档（详细API说明）
├── 轻商城litemall.xlsx # 接口测试用例数据
└── 轻商城接口测试.xmind # 测试用例思维导图

## 地址配置
BASE_URL = "http://www.litemall360.com:8080"   # 系统接口域名
WEB_URL = "http://www.litemall360.com:8082"    # 商城前端地址
ADMIN_URL = "http://www.litemall360.com:8081"  # 管理后台地址

## 运行完后在终端输入获取报告
allure serve report
