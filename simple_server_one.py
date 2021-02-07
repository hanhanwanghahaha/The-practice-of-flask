# coding:utf-8

# 步骤：
# 搭建服务
# 监听动作 while循环，每隔几秒钟要去看看有没有请求发过来
# 处理程序
# 返回数据到套接字，生成一个响应对象
from wsgiref.simple_server import make_server


def app(env, make_reponse):
    # env 获取相关数据——环境变量
    # make_reponse(状态码：header)
    make_reponse("200 ok", [('content-type', 'text/plain')])
    return [b"hello,hanhanwang"]  # b为byte类型


server = make_server("", 8002, app)
server.serve_forever()