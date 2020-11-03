import requests
import json
# import crypt
import rsa
# import pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from public import  Encrypt
import time
from public.Encrypt import EncryptByAES
from public.Encrypt import md5
from public import DataDeal

serverAddr = "http://10.9.244.117"
rsapubUrl = "/sl/v2/rsapub"
loginUrl = "/sl/v2/login"

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
        print(rsapubRts.content.decode("utf-8"))
        return rsapubRtsJson["data"]
    else:
        print(rsapubRtsJson["desc"])
        print("get RsaPub Failed!")
    # print()

def get_token(serverAdd,loginUrl,rsaPubInfo,secret,passwd,account):
    print(rsaPubInfo)
    captchacode = 0
    empoent = rsaPubInfo["empoent"]
    module = rsaPubInfo["module"]
    rsa_id = rsaPubInfo["rsa_id"]
    rsa_id1 = "slkv2-rsaid-h4GaLZTNKMFQV4T6"
    passwd = passwd
    EnpasswdAES = EncryptByAES(empoent,module,passwd)
    enpasswd = EnpasswdAES.encrypt_with_pubkey(passwd)
    # print(enpasswd)
    # enpasswd1="6712eb247223e630ce31d6267ece93824c28c5db8e42aa08569e3e35c966366b4967edbfcddc727a16f1ccf9f5284816f40f233dfc929d2618ca3ca4849a2470f325291043b3b2db63fe4059276029b6d90e95545254b5a03dd2103ec420299772689287edc323a7c7769a9b4409af84e7a30086a789e2f2cde5675bd7afe422"
    loginHeaders = {"LANGUAGE": "zh",
                    "CHANNEL": "1"}
    if captchacode:
        loginParams = {
            'account': account,
            'password': enpasswd,
            'rsa_id': rsa_id,
            'csessionid': "ewrtwertwert",
            'scene': "login",
            'sig': "2ad0557fc8ff5bf1c4d5f0f7c9395492"
        }
    else:
        loginParams = {
            'account': account,
            'password': enpasswd,
            'rsa_id': rsa_id
        }
    print(loginParams)
    testloginRts = requests.post(serverAdd+loginUrl,headers=loginHeaders,json=loginParams,verify=False)
    # testloginRts1 = requests.post(serverAdd + loginUrl, headers=loginHeaders, json=loginParams1, verify=False)
    print(testloginRts.content.decode("utf-8"))
    print("&&&&&&&&&&&&&&&&")
    if testloginRts.status_code == 200:
        print(testloginRts.content.decode("utf-8"))
        logginRts = json.loads(testloginRts.content)
        # return logginRts['data']
    else:
        print("get Token Failed!")
    # print(testloginRts1.content.decode("utf-8"))
    if testloginRts.status_code == "200":
        login_token = logginRts['data']['token']
        timestamp = int(time.time()*1000)
        print(timestamp)
        sign = md5("AUTH-TIMESTAMP=" + str(timestamp) + "&AUTH-TOKEN=" + login_token+ "#" + secret)
        headers = {"LANGUAGE": "zh", "AUTH-TIMESTAMP": str(timestamp), "AUTH-TOKEN": login_token,
                        "AUTH-SIGN": sign, 'Referer': serverAdd + '/sign/signRecord', 'TIME-ZONE': 'GMT+08:00'}
        tmpheader = {"login_token":login_token,
                     "request_headers":headers,
                     "timestamp":str(timestamp)
        }
        return tmpheader
    else:
        print("get token failed！")
        print(testloginRts.content.decode("utf-8"))

def face_login(serverAdd,mobile,areacode,cap_photo,company_id,secret,passwd,account):
    timestamp = int(time.time() * 1000)
    print("face_login")
    faceloginUrl = "/sl/v2/staff/face/login"
    rsapubRts = get_rsapub(serverAdd,rsapubUrl)
    # testheader = get_token(serverAdd,faceloginUrl,rsapubRts,secret,passwd,account)
    # params = {'mobile':'15507558325',
    #           'area_code':'86',
    #           'cap_photo':self.loginavater,
    #           'company_id':1
    # }
    params = {'mobile':mobile,
              'area_code':areacode,
              'cap_photo':cap_photo,
              'company_id':company_id
    }
    # print(params)
    header = {}
    testLoginRts = requests.post(serverAdd+faceloginUrl,headers = header,json = params,verify=False)
    # print(testLoginRts.content.decode('utf-8'))
    testLoginJson = json.loads(testLoginRts.content)
    print(testLoginJson)
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

def device_login(serverAdd,loginUrl,rsaPubinfo,identifier,duid,passwd,account):
    print(rsaPubinfo)
    captchacode = 0
    empoent = rsaPubinfo["empoent"]
    module = rsaPubinfo["module"]
    rsa_id = rsaPubinfo["rsa_id"]
    # passwd = passwd
    EnpasswdAES = EncryptByAES(empoent,module,passwd)
    enpasswd = EnpasswdAES.encrypt_with_pubkey(passwd)
    # print(enpasswd)
    # enpasswd1="6712eb247223e630ce31d6267ece93824c28c5db8e42aa08569e3e35c966366b4967edbfcddc727a16f1ccf9f5284816f40f233dfc929d2618ca3ca4849a2470f325291043b3b2db63fe4059276029b6d90e95545254b5a03dd2103ec420299772689287edc323a7c7769a9b4409af84e7a30086a789e2f2cde5675bd7afe422"
    loginHeaders = {"LANGUAGE": "zh"}
    params = {
        'rsa_id': rsa_id,
        'account': account,
        'password': enpasswd,
        'identifier': identifier,
        'duid': duid
    }
    timestamp = int(time.time() * 1000)
    # print(params)
    login_rts = requests.post(serverAdd+loginUrl,json=params,headers = loginHeaders,verify=False)
    if login_rts.status_code == 200:
        login_info = {
            "timestamp":str(timestamp),
            "device_logininfo":json.loads(login_rts.content)['data']
        }
        # print(login_rts.content.decode("utf-8"))
        return login_info
    else:
        print("Device login failed!")
        return

if __name__ == "__main__":
    # face_login(self, serverAdd, mobile, areacode, cap_photo, company_id, secret, passwd, account)
    passwd = "Admin1234@"
    account = "bitest"
    secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
    serveradd = "https://link-stage.bi.sensetime.com"
    login_avatar = DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg")
    face_login("https://link-stage.bi.sensetime.com","15507558325","86",login_avatar,1,secret,passwd,account)
    print("((((((((((((((((((((")
    rsapubRts=get_rsapub(serveradd,rsapubUrl)
    device_loginRts = device_login(serveradd,"/sl/v2/device/login",rsapubRts,"SPSE","SPSE-c81e728d9d4c2f636f067f89cc14862c","Admin1234","admin1234")
    print(device_loginRts)
    # print(get_token(serverAddr,loginUrl,rsapubRts,"bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"))