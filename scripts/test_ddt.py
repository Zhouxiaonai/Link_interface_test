import unittest
import ddt
from ddt import ddt,data,unpack,file_data

"""
@ddt  #装饰测试类
class TestHttp(unittest.TestCase):
    def setUp(self):
        print ('ceshi')

    @data(*test_data)    #装饰测试方法，拿到几个数据，就执行几条用例
    def test_api(self,item):  #接口用例
            res = HttpRequest().http_request(item['url'],item['data'],item['method'],getattr(GetData,'Cookie'))
            if res.cookies:
                setattr(GetData,'Cookie',res.cookies)
            try:
                self.assertEqual(item['expected'],res.json()['status'])
            except AssertionError as e:
                print ('test api error is {}'.format(e))
                raise e
            print res.json()
"""


mydata = [{'sd':'lili','age':12},{'sd':'KK','age':'teacher'}]

@ddt
class TestParams(unittest.TestCase):
    def setUp(self):
        print("set up!")

    def tearDown(self):
        print("tear down!")
    @file_data(r"D:\tasks\SenseLink\testddt.json")
    @unpack
    def test_ddt(self,search_key,name):
        print(search_key)
        print(name)
        # print(item['name'])
        # print(item['age'])
        # print(value1)
        # print(value[0]['name'])
    pass

if __name__ == "__main__":
    testsuite = unittest.TestSuite
    testsuite.addTest(TestParams("test_ddt"))
    runner = unittest.TestRunner
    runner.run(testsuite)