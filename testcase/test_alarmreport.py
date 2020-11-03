import requests
import os
import sys
import unittest
from scripts import Login
from public.Encrypt import md5
import time
import HTMLTestRunner
import ddt
from ddt import data,file_data,unpack,ddt
from public import GetSign
import random

tmptimestamp = str(int(time.time() * 1000))
# serveradd = "http://10.9.66.122"
serveradd = "http://10.9.244.116"
rsaurl = "/sl/v2/rsapub"
loginurl = "/sl/v2/device/login"
secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
testurl = "/sl/v2/device/alarm/report"
params = {'device_id': "SPS020STDC19E01313",
          'package_name': "com.sensetime.sensepassproe",
          'version_code': 24,
          'version_name': "1.1.4_E",
          'timestamp': tmptimestamp
          }

@ddt
class TestAlarmReport(unittest.TestCase):
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
        self.passwd = "admin1234"
        self.account = "admin1234"
        self.params = params
        self.regist = "/sl/v2/device/register"
        print("start")
        # print(self.params)
        pass

    @file_data(r"C:\Users\zhouwenchao\PycharmProjects\SenseLink_interfacetest\testdata\testddt_alarmreport.json")
    def test_alarmreport(self,trace_id,description,code,user_id,event_time,status,alarm_photo,rectangle,x,y):
        rsapubRts = Login.get_rsapub(self.serveradd,self.rsaurl)
        testheader = Login.device_login(self.serveradd,self.loginurl,rsapubRts,"SPSX","Xtest","admin1234","admin1234")
        # self.params['timestamp'] = testheader['timestamp']
        print(testheader)
        print(testheader['device_logininfo']['device']['ldid'])
        ldid = testheader['device_logininfo']['device']['ldid']
        # params = {}
        # params['trace_id'] = str(int(time.time()*1000))
        # params['description'] = description
        # params['code'] = code
        # params['user_id'] = user_id
        # params['event_time'] = testheader['timestamp']
        # params['status'] = status
        # # print(sorted(params.items(), key=lambda d: d[0], reverse=False))
        # tmpsignOri = sorted(params.items(), key=lambda d: d[0], reverse=False)
        # mystr = ""
        # for item in tmpsignOri:
        #     mystr = mystr+"&"+str(item[0])+"="+str(item[1])
        # mystrFal = mystr + "#" + self.secret
        # # print(mystrFal[1:-1])
        # tmpsign = md5(mystrFal[1:])
        headers = {
            "LANGUAGE": "en",
            'AUTH-TIMESTAMP': testheader['timestamp'],
            'AUTH-TOKEN': testheader['device_logininfo']['token'],
            'LDID': ldid,
            'AUTH-SIGN': GetSign.get_sign(testheader['timestamp'],testheader['device_logininfo']['token']),
            'Referer': 'http://www.sensetime.com'
        }
        # +testheader['timestamp'][-4:]
        params = {'trace_id':"SPX-"+testheader['timestamp']+"-001-72BAAW",
                  'code':code,
                  'event_time':testheader['timestamp'],
                  'status':1,
                  'description':description
                  }
        paramsRes = {
            "description":"PassXtest",
            "direction":"1",
            "info":"PassXtest",
            "name":"PassXtest",
            "software_version":"v1.11.0"
        }
        print("*******************************")
        print(headers)
        print(params)
        regRts = requests.post(self.serveradd+self.regist,headers=headers, json=paramsRes, verify=False)
        testRts = requests.post(self.serveradd+self.testurl,headers=headers, json=params, verify=False)
        print(regRts.content.decode("utf-8"))
        print(testRts.content.decode("utf-8"))
        pass

    def tearDown(self):
        print("end")
        print("*************************")
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
    testsuite = unittest.TestSuite()
    # testAppUpdate = TestAPPUpdate(serveradd,rsaurl,loginurl,secret,testurl,params)
    # testAppUpdate.test_appupdate()
    testsuite.addTest(TestAlarmReport('test_alarmreport'))
    runner = unittest.TestRunner()
    runner.run(testsuite)
    pass