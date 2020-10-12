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
from nose_parameterized import parameterized
import ddt

tmptimestamp = str(int(time.time() * 1000))
serveradd = "https://link-stage.bi.sensetime.com"
rsaurl = "/sl/v2/rsapub"
loginurl = "/sl/v2/login"
secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
testurl = "/sl/v2/record/shi"
params = {'device_id': "SPS020STDC19E01313",
          'package_name': "com.sensetime.sensepassproe",
          'version_code': 24,
          'version_name': "1.1.4_E",
          'timestamp': tmptimestamp
          }
# on_business=random.randint(0,1)
on_business= 3
country_code = "CN"
place_code = "440305"
address = "ShenzhenBay"
platform = 5 #random.randint(1,2)
attendance_area_id = 202
remark = "Remark"
entry_mode = random.randint(1,4)
server_identify = 1
passwd = "Admin1234@"
account = "bitest"
sign_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\loginme.jpg")
# sign_bg_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg")
# login_avatar = DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg")
#noliving.jpg
sign_bg_avatar= DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\5f704552f54fd90001ee6a06.jpg")
login_avatar = DataDeal.get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\登录人脸\loginme.jpg")

testdata = [{},
            {},
            {}]

def test_mobileexist(header):
    params = {'mobile': '15507558325'}
    header = {}
    testrts = requests.post(serveradd + "/v2/staff/check/exist", headers=header, json=params, verify=False)
    print(testrts.content)
    pass

# @ddt.ddt
class TestRecordUp(unittest.TestCase):
    # def __init__(self,serveradd,rsaurl,loginurl,secret,testurl,params):
    #     self.serveradd = serveradd
    #     self.rsaurl = rsaurl
    #     self.loginurl = loginurl
    #     self.secret = secret
    #     self.testurl = testurl
    #     self.params = params
    #     pass

    def setUp(self):
        self.serveradd = serveradd
        self.rsaurl = rsaurl
        self.loginurl = loginurl
        self.secret = secret
        self.testurl = testurl
        self.params = params
        self.sign_avatar = ""#sign_avatar
        self.sign_bg_avatar = sign_bg_avatar
        self.latitude = ""#"22.55329"
        self.longitude = "113.88308"
        self.on_business = 5 #on_business
        self.country_code = ""#country_code
        self.place_code = ""#place_code
        self.address= address
        self.platform= platform
        self.attendance_area_id= attendance_area_id
        self.remark= remark
        self.entry_mode= 5 #entry_mode
        self.server_identify= ""#server_identify
        self.passwd = passwd
        self.account = account
        self.mobile = "15507558889"
        self.loginavater = login_avatar
        self.company = 5
        print("start")
        # print(self.params)
        pass

    def test_uprecord(self):
        print("test_uprecord!!!")
        rsapubRts = Login.get_rsapub(self.serveradd,self.rsaurl)
        # mytoken = Login.face_login(self.mobile,self.country_code,self.loginavater,self.company)
        # testheader = Login.get_token(self.serveradd,self.loginurl,rsapubRts,self.secret,self.passwd,self.account)
        # face_login("https://link-stage.bi.sensetime.com", "15507558325", "86", login_avatar, 1, secret, passwd, account)
        testheader = Login.face_login(self.serveradd,self.mobile,self.country_code,self.loginavater,self.company,self.secret,self.passwd,self.account)
        print(testheader)
        self.params['timestamp'] = testheader['timestamp']
        # print(sorted(self.params.items(), key=lambda d: d[0], reverse=False))
        # tmpsignOri = sorted(self.params.items(), key=lambda d: d[0], reverse=False)
        # mystr = ""
        # for item in tmpsignOri:
        #     mystr = mystr+"&"+str(item[0])+"="+str(item[1])
        # mystrFal = mystr + "#" + self.secret
        # print(mystrFal[1:-1])
        # tmpsign = md5(mystrFal[1:])
        # test_mobileexist(testheader['request_headers'])
        params = {'sign_avatar':self.sign_avatar,
                  'sign_bg_avatar':self.sign_bg_avatar,
                  'latitude':self.latitude,
                  'longitude':self.longitude,
                  'on_business':self.on_business,
                  'country_code':self.country_code,
                  'place_code':self.place_code,
                  'address':self.address,
                  'platform': self.platform,
                  'attendance_area_id': self.attendance_area_id,
                  'remark': self.remark,
                  'entry_mode': self.entry_mode,
                  'server_identify':self.server_identify
                  }
        print(params)
        header={}
        # testRts = requests.post(self.serveradd+self.testurl,headers = testheader['request_headers'], json=params)
        testRts = requests.post(self.serveradd+self.testurl,headers = testheader["request_headers"], json=params,verify=False)
        print(testRts.content.decode('utf-8'))
        pass

    def tearDown(self):
        print("end")
        pass
    pass

if __name__ == "__main__":
    # unittest.main()
    # serveradd = "http://10.9.244.117"
    # rsaurl = "/sl/v2/rsapub"
    # loginurl = "/sl/v2/login"
    # secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
    # testurl = "/fs/v1/upgrade_app"
    # params = {'device_id':"SPSPE-395db7f7b22f13df12e21574a429455e",
    #           'package_name':"com.sensetime.sensepassproe",
    #           'version_code':"1.1.4_E",
    #           'version_name':"24",
    #            'timestamp':int(time.time()*1000)
    #     }
    test_mobileexist()
    testsuite = unittest.TestSuite()
    # testAppUpdate = TestAPPUpdate(serveradd,rsaurl,loginurl,secret,testurl,params)
    # testAppUpdate.test_appupdate()
    # testsuite.addTest(TestRecordUp('test_mobileexist'))
    # testsuite.addTest(TestRecordUp('test_uprecord'))
    # testsuite.addTest(TestRecordUp('test_face_lgoin'))
    testsuite.addTest(TestRecordUp('test_getrecord'))
    runner = unittest.TestRunner()
    runner.run(testsuite)
    pass