import requests
import json

s = requests.session()

url = "http://192.168.15.201:8082/user/login"

body = {
    "loginCode":"admin",
    "loginPwd":"admin",
}

# 请求登陆接口
r = s.post(url,json=body)
print(r.text)
# 获取登录的token
token = r.json()["entity"]["api_token"]
print("获取到登录的token:%s" % token)
h2 = {
    "api_token": token
}

# 没有更新之前的seccion头部
print("没有更新之前session头部:%s" % s.headers)
# 更新头部
s.headers.update(h2)

url2 = "http://192.168.15.201:8082/user/getCurrentUser"

r2 = requests.get(url=url2,h2=h2)

print(r2.text)