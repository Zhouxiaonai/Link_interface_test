import requests
import hashlib
import time
import json

nowtime = lambda: int(round(time.time() * 1000))
timestamp = str(nowtime())

#修改secret
def get_sign():
    SECRET = '73e17e142e06125d272e94537e19756a'
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


# url = 'http://link-test.bi.sensetime.com'
# url = 'http://127.0.0.1:8099'
#修改服务器地址
url = "http://10.9.244.116"

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://172.20.5.57",
}

#修改/key
getdata = {
    "name": "1312313123123122",
    "mobile": "",
    "remark": "",
    # "type": '1',
    "icNumber": "123412000",
    "jobNumber": "12012003",
    # "duid":"",
    "sign": get_sign(),
    "app_key": "8a4bad370696b9af",
    "timestamp": timestamp,
}
# response = requests.post(url+"/api/v2/device/register?"+get_para(getdata), data=json.dumps(postdata), headers=headers)
print(get_para(getdata))
response = requests.post(url + "/api/v2/user/update/79653?groups=118&" + get_para(getdata), headers=headers)
print(response.text)

# for i in range(107887,117887):
    #107865,107882
for i in range(107865,117883):
    getdatax = {
        "remark": "",
        "sign": get_sign(),
        "app_key": "8a4bad370696b9af",
        "timestamp": timestamp,
    }
    mvdatax = {
        "groupId": "118",
        "userIds": str(i),
        "sign": get_sign(),
        "app_key": "8a4bad370696b9af",
        "timestamp": timestamp
    }
    # responsemv = requests.post(url + "/api/v1/user/remove/group?" + get_para(mvdatax), headers=headers)
    responsex = requests.post(url + "/api/v2/user/update/"+str(i)+"?groups=126&groups=3&" + get_para(getdatax), headers=headers)
    print(responsex.text)
    pass