import requests
import hashlib
import time

nowtime = lambda: int(round(time.time() * 1000))
timestamp = str(nowtime())


def get_sign():
    SECRET = '24daf37e02dca1de477a4c0aefb31b8e'
    md5 = timestamp + "#" + SECRET
    m1 = hashlib.md5()
    m1.update(md5.encode("utf-8"))
    sign = m1.hexdigest()
    return sign


def get_para(object):
    str1 = ""
    for obj in object.items():
        key, value = obj
        str1 = str1 + key + "=" + value + "&"
    str1 = str1[:-1]
    return str1


url = 'http://link-stage.bi.sensetime.com'

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://172.20.5.57",
}
postdata = {
    "sign": get_sign(),
    "app_key": "dba4d6b2cb70282b",
    "timestamp": timestamp,
}

response = requests.get(url + "/api/v3/record/list?" + get_para(postdata), headers=headers)
print(response.text)