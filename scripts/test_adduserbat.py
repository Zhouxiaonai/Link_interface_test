import requests
import hashlib
import time
import json
import os
from public.DataDeal import get_pic_base64

nowtime = lambda: int(round(time.time() * 1000))
timestamp = str(nowtime())

def get_sign():
    SECRET = '24daf37e02dca1de477a4c0aefb31b8e'#24daf37e02dca1de477a4c0aefb31b8e
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

# url = 'https://link-stage.bi.sensetime.com'
url = 'https://link-stage.bi.sensetime.com'
# url = 'http://127.0.0.1:8099'

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://172.20.5.57",
}

getdata = {
    "name": "1312313123123122",
    "mobile": "15576761233",
    "remark": "",
    # "type": '1',
    "icNumber": "1234030120",
    "jobNumber": "120132003",
    # "duid":"",
    "sign": get_sign(),
    "app_key": "dba4d6b2cb70282b",
    "timestamp": timestamp,
}

f = open(r"E:\picture\5w底图\117004542.jpeg",'rb')
files = {"avatarFile":(r"E:\picture\5w底图\117004542.jpeg",f,"image/jprg")}
# response = requests.post(url+"/api/v2/device/register?"+get_para(body), data=json.dumps(postdata), headers=headers)
# print(get_para(getdata))
response = requests.post(url + "/api/v1/user",data=getdata,files=files,headers=headers)
print(getdata)
print(files)
# response = requests.post(url + "/api/v1/user?groups=15612&groups=15615&" + get_para(getdata),headers=headers)
print(response.text)

def add_user_bat():
    AllPic = os.listdir(r"E:\picture\5w底图")
    for j in range(0,len(os.listdir(r"E:\picture\5w底图"))):
        filef = open(AllPic[j],"rb")
        files =("avatarFile",filef,"image/jpeg")
        print(AllPic[j])
        getdataX = {
            "name": "testname"+str(j),
            "mobile": "1576767"+str(j),
            "remark": "",
            # "type": '1',
            "icNumber": "12340200",
            "jobNumber": "1200203",
            # "duid":"",
            "avatarFile":AllPic[j],
            "sign": get_sign(),
            "app_key": "dba4d6b2cb70282b",
            "timestamp": timestamp,
        }
        print(get_para(getdataX))
        response = requests.post(url + "/api/v1/user?groups=15612&groups=15615&" + get_para(getdataX),files=files, headers=headers)
        print(response.text)