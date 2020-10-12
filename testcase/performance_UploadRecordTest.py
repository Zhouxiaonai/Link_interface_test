import requests
import os
import sys
import unittest
from scripts import Login
from public.Encrypt import md5
import time
import random
import HTMLTestRunner
from public import DataDeal
import parameterized
# from nose_parameterized import parameterized
import ddt
import json
import yaml
from public import Encrypt
from scripts import Login
import threading

tmptimestamp = str(int(time.time() * 1000))
serveradd = "https://link-stage.bi.sensetime.com"
rsaurl = "/sl/v2/rsapub"
loginurl = "/sl/v2/login"
secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
testurl = "/sl/v2/record/shi"
# params = {'device_id': "SPS020STDC19E01313",
#           'package_name': "com.sensetime.sensepassproe",
#           'version_code': 24,
#           'version_name': "1.1.4_E",
#           'timestamp': tmptimestamp
#           }
# on_business=random.randint(0,1)
on_business= 0
country_code = "CN"
place_code = "440305"
address = "ShenzhenBay"
platform = random.randint(1,2)
attendance_area_id = 202
remark = "Remark"
entry_mode = random.randint(1,4)
server_identify = 1
passwd = "Admin1234@"
account = "bitest"
mobile="15507558889"
company=5
latitude=""
longitude=""

myparams = {'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'22.55329',
               'longitude':'113.88308',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558889',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
            }

sign_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg")
# sign_bg_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg")
# login_avatar = DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg")
#noliving.jpg #
sign_bg_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg")
loginavater = DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\noface.jpg.jpg")

with open(r"D:\tasks\SenseLink\测试数据\parameters.yaml",encoding='utf-8') as df:
    datalist = yaml.load(df,Loader=yaml.FullLoader)

def get_rsapub(serverAdd,url):
    headers = {}
    params = {}
    rsapubRts = requests.get(serverAdd+url,headers=headers,params=params)
    rsapubRtsJson = json.loads(rsapubRts.content)
    # print(serverAdd+url)
    if rsapubRts.status_code == 200:
        # print(rsapubRts.content)
        rsapubRtsJson = json.loads(rsapubRts.content)
        rsapubRtsJson = json.loads(rsapubRts.content)
        # print(rsapubRtsJson["data"])
        return rsapubRtsJson["data"]
    else:
        print(rsapubRtsJson["desc"])
        print("get RsaPub Failed!")

# def face_login(serverAdd,mobile,areacode,cap_photo,company_id,secret,passwd,account,rsapubUrl):
#     timestamp = int(time.time() * 1000)
#     print("face_login")
#     faceloginUrl = "/sl/v2/staff/face/login"
#     rsapubRts = get_rsapub(serverAdd,rsapubUrl)
#     # testheader = get_token(serverAdd,faceloginUrl,rsapubRts,secret,passwd,account)
#     # params = {'mobile':'15507558325',
#     #           'area_code':'86',
#     #           'cap_photo':self.loginavater,
#     #           'company_id':1
#     # }
#     params = {'mobile':mobile,
#               'area_code':areacode,
#               'cap_photo':cap_photo,
#               'company_id':company_id
#     }
#     # print(params)
#     header = {}
#     testLoginRts = requests.post(serverAdd+faceloginUrl,headers = header,json = params,verify=False)
#     # print(testLoginRts.content.decode('utf-8'))
#     testLoginJson = json.loads(testLoginRts.content)
#     sign = md5("AUTH-TIMESTAMP=" + str(timestamp) + "&AUTH-TOKEN=" + testLoginJson['data']['token'] + "#" + secret)
#     headers = {
#         "LANGUAGE": "en",
#         "AUTH-TIMESTAMP": str(timestamp),
#         "AUTH-TOKEN":  testLoginJson['data']['token'] ,
#         "AUTH-SIGN": sign,
#         "Referer": "http://www.sensetime.com"
#     }
#     tmpheader = {"login_token": testLoginJson['data']['token'] ,
#                  "request_headers":headers,
#                  "timestamp":str(timestamp)
#     }
#     # print(tmpheader)
#     return tmpheader

def face_login(loginParam):
    print(loginParam)
    timestamp = int(time.time() * 1000)
    print("face_login")
    faceloginUrl = "/sl/v2/staff/face/login"
    rsapubRts = get_rsapub(loginParam['serverAdd'],loginParam['rsapubUrl'])
    # testheader = get_token(serverAdd,faceloginUrl,rsapubRts,secret,passwd,account)
    # params = {'mobile':'15507558325',
    #           'area_code':'86',
    #           'cap_photo':self.loginavater,
    #           'company_id':1
    # }
    params = {'mobile':loginParam['mobile'],
              'area_code':loginParam['areacode'],
              'cap_photo':loginParam['cap_photo'],
              'company_id':loginParam['company_id']
    }
    # print(params)
    header = {}
    testLoginRts = requests.post(loginParam['serverAdd']+faceloginUrl,headers = header,json = params,verify=False)
    # print(testLoginRts.content.decode('utf-8'))
    testLoginJson = json.loads(testLoginRts.content)
    sign = md5("AUTH-TIMESTAMP=" + str(timestamp) + "&AUTH-TOKEN=" + testLoginJson['data']['token'] + "#" + secret)
    headers = {
        "LANGUAGE": "en",
        "AUTH-TIMESTAMP": str(timestamp),
        "AUTH-TOKEN":  testLoginJson['data']['token'] ,
        "AUTH-SIGN": sign,
        "Referer": "http://www.sensetime.com"
    }
    tmpheader = {"login_token": testLoginJson['data']['token'] ,
                 "request_headers":headers,
                 "timestamp":str(timestamp)
    }
    # print(tmpheader)
    return tmpheader

def test_uprecord(params):
    print("test_uprecord!!!")
    rsapubRts = Login.get_rsapub(params['serveradd'], params['rsaurl'])
    testheader = Login.face_login(params['serveradd'], params['mobile'], params['country_code'], params['loginavater'], params['company'],
                                  params['secret'], params['passwd'], params['account'])
    params = {'sign_avatar': params['sign_avatar'],
              'sign_bg_avatar': params['sign_bg_avatar'],
              'latitude': params['latitude'],
              'longitude': params['longitude'],
              'on_business': params['on_business'],
              'country_code': params['country_code'],
              'place_code': params['place_code'],
              'address': params['address'],
              'platform': params['platform'],
              'attendance_area_id': params['attendance_area_id'],
              'remark': params['remark'],
              'entry_mode': params['entry_mode'],
              'server_identify': params['server_identify']
              }
    # print(params)
    header = {}
    # testRts = requests.post(serveradd+testurl,headers = testheader['request_headers'], json=params)
    testRts = requests.post(serveradd + testurl, headers=testheader["request_headers"], json=params,
                            verify=False)
    print(testRts.content.decode('utf-8'))

def sign_record(sign_param,record_param):
    print(sign_param)
    face_login(sign_param)
    test_uprecord(record_param)
    pass

# def test_uprecord(serveradd,rsaurl,mobile,country_code,loginavater,company,secret,testurl,passwd,account,sign_avatar,sign_bg_avatar,latitude,longitude,on_business,place_code,address,platform,attendance_area_id,remark,entry_mode,server_identify):
#     print("test_uprecord!!!")
#     rsapubRts = Login.get_rsapub(serveradd, rsaurl)
#     testheader = Login.face_login(serveradd, mobile, country_code, loginavater, company,
#                                   secret, passwd, account)
#     params = {'sign_avatar': sign_avatar,
#               'sign_bg_avatar': sign_bg_avatar,
#               'latitude': latitude,
#               'longitude': longitude,
#               'on_business': on_business,
#               'country_code': country_code,
#               'place_code': place_code,
#               'address': address,
#               'platform': platform,
#               'attendance_area_id': attendance_area_id,
#               'remark': remark,
#               'entry_mode': entry_mode,
#               'server_identify': server_identify
#               }
#     # print(params)
#     header = {}
#     # testRts = requests.post(serveradd+testurl,headers = testheader['request_headers'], json=params)
#     testRts = requests.post(serveradd + testurl, headers=testheader["request_headers"], json=params,
#                             verify=False)
#     print(testRts.content.decode('utf-8'))

# test_uprecord(serveradd,rsaurl,mobile,country_code,loginavater,company,secret,testurl,passwd,account,sign_avatar,sign_bg_avatar,latitude,longitude,on_business,place_code,address,platform,attendance_area_id,remark,entry_mode,server_identify)
# test_uprecord(testcaselist[0])

signparam1 = [{'serverAdd':'https://link-stage.bi.sensetime.com','mobile':'15507558325','areacode':'440305','cap_photo': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),'company_id':5,'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8','passwd':'','account':'','rsapubUrl':'/sl/v2/rsapub'}]
signparam = {'serverAdd':'https://link-stage.bi.sensetime.com','mobile':'15507558325','areacode':'440305','cap_photo': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),'company_id':5,'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8','passwd':'','account':'','rsapubUrl':'/sl/v2/rsapub'}

# face_login(signparam)

testcaselist0 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'22.55329',
               'longitude':'113.88308',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':random.randint(0,2),
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558889',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]
testcaselist1 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'sdfjkaf',
               'longitude':'113.88308',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558889',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]
testcaselist2 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'22.55329',
               'longitude':'asdkfjskdf',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558889',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]
testcaselist3 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'',
               'longitude':'113.88308',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558889',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]
testcaselist4 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'22.55329',
               'longitude':'',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhenBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558325',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]
testcaselist5 = [{'serveradd':'https://link-stage.bi.sensetime.com',
               'rsaurl':'/sl/v2/rsapub',
               'loginurl':'/sl/v2/login',
               'secret':'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8',
               'testurl':'/sl/v2/record/shi',
               'sign_avatar':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg"),
               'sign_bg_avatar': DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg"),
               'latitude':'22.55329',
               'longitude':'113.88308',
               'on_business':1,
               'country_code':'CN',
               'place_code':'440305',
               'address':'ShenzhesakdfjkasdjfkajdfklajdflaksjdflajsdfklajsdklfjasldfjlasfdjlkasjfdlajsdkflnBay',
               'platform':1,
               'attendance_area_id':202,
               'passwd':'Admin1234@',
               'account':'bitest',
               'mobile':'15507558325',
               'remark':'',
               'company':5,
               'loginavater':DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg"),
                'entry_mode':random.randint(1,4),
                'server_identify':1
                }]

# test_uprecord(testcaselist0[0])

threads = []
for i in range(0,20):
    # print(type(testcaselist[i]))
    # t=threading.Thread(target=face_login,args=(signparam1))
    # t = threading.Thread(target=test_uprecord, args=(testcaselist0))
    t=threading.Thread(target=sign_record,args=(signparam,testcaselist0[0]))
    threads.append(t)

if __name__ == "__main__":
    start_time = time.time()
    for i in range(0,20):
        threads[i].start()
    for i in range(0,20):
        threads[i].join()
    end_time = time.time()
    print("runtime="+str(end_time-start_time))