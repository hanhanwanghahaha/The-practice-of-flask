# coding:utf-8

# 步骤：
# 搭建服务
# 监听动作 while循环，每隔几秒钟要去看看有没有请求发过来
# 处理程序
# 返回数据到套接字，生成一个响应对象
from wsgiref.simple_server import make_server


def index():
    return "hello,I'm index!"


def register():
    return "hello,please register!"


def login():
    return "hello,please login!"


# 这是一段路由 集中管理（有点像Django框架）
patterns = {
    "/": index,
    "/register": register,
    "/login": login,
}


def app(env, start_resp):
    # env 获取相关数据——环境变量
    # start_resp(状态码：header)

    url = env.get("PATH_INFO")
    if (url is None) or (url not in patterns.keys()):
        start_resp("404 not found", [('content-type', 'text/plain')])
        return [b"sorry!page not found!"]  # b为byte类型

    start_resp("200 ok", [('content-type', 'text/plain')])
    respon = patterns.get(url)
    if respon is None:
        start_resp("404 not found", [('content-type', 'text/plain')])
        return [b"sorry!page not found!"]  # b为byte类型

    return [respon().encode()]


server = make_server("", 8001, app)
server.serve_forever()