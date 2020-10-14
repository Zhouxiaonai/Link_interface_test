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

tmptimestamp = str(int(time.time() * 1000))
serveradd = "http://10.9.244.116"
rsaurl = "/sl/v2/rsapub"
loginurl = "/sl/v2/login"
secret = "bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
testurl = "/fs/v1/upgrade_app"
params = {'device_id': "SPS020STDC19E01313",
          'package_name': "com.sensetime.sensepassproe",
          'version_code': 24,
          'version_name': "1.1.4_E",
          'timestamp': tmptimestamp
          }
testdata = [{},{}]

@ddt
class TestAPPUpdate(unittest.TestCase):
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
        print("start")
        # print(self.params)
        pass

    @file_data(r"C:\Users\zhouwenchao\PycharmProjects\SenseLink_interfacetest\testdata\testddt_linkapp.json")
    def test_appupdateA(self,device_id,package_name,version_code,version_name):
        rsapubRts = Login.get_rsapub(self.serveradd,self.rsaurl)
        testheader = Login.get_token(self.serveradd,self.loginurl,rsapubRts,self.secret,self.passwd,self.account)
        self.params['timestamp'] = testheader['timestamp']
        params = {}
        params['device_id'] = device_id
        params['package_name'] = package_name
        params['version_code'] = version_code
        params['version_name'] = version_name
        params['timestamp'] = testheader['timestamp']
        # print(sorted(params.items(), key=lambda d: d[0], reverse=False))
        tmpsignOri = sorted(params.items(), key=lambda d: d[0], reverse=False)
        mystr = ""
        for item in tmpsignOri:
            mystr = mystr+"&"+str(item[0])+"="+str(item[1])
        mystrFal = mystr + "#" + self.secret
        # print(mystrFal[1:-1])
        tmpsign = md5(mystrFal[1:])

        params = {'device_id':device_id,
                  'package_name':package_name,
                  'version_code':version_code,
                  'version_name':version_name,
                  'timestamp':params['timestamp'],
                  'sign':tmpsign
                  }
        # print(params)
        header={}
        testRts = requests.post(self.serveradd+self.testurl,headers = header, json=params)
        print(testRts.content)
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
    testsuite.addTest(TestAPPUpdate('test_appupdateA'))
    runner = unittest.TestRunner()
    runner.run(testsuite)
    pass