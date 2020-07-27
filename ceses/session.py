import requests
import pytest
import re
# 创建浏览器
s = requests.session()

web_url = "http://49.235.92.12:6009/admin/login/?next=/admin/"

r = s.get(url=web_url)

# print(r.text)

token = re.findall("'csrfmiddlewaretoken' value='(.+?)'",r.text)
# print(token)

body = {
    "csrfmiddlewaretoken":token,
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/",
}

r1 = s.post(url=web_url,data=body)

# print(r1.text)
assert "Site administration | Django site admin" in r1.text