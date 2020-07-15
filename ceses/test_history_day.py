import requests
import pytest
host = "http://api.juheapi.com"
def test_historyDay():
    apiurl = "/japi/toh"

    params = {
        "key": "cf022158ea25a59fad95447b4c4f6085",
        "v": "1.0",
        "month": 7,
        "day": 15,
    }

    r = requests.get(host+apiurl,params=params)

    # print(r.text)

    assert r.json()["error_code"] == 0
    assert r.json()["reason"] == "请求成功！"
    assert r.json()["result"]

if __name__ == '__main__':
    pytest.main(["-s","test_history_day.py"])