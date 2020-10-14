import unittest
import os
from HTMLTestRunner import HTMLTestRunner

casepath = os.path.join(os.getcwd(),"testcase")
reportpath = os.path.join(os.getcwd(),"report")

def all_case():
    dicover = unittest.defaultTestLoader.discover(casepath,pattern="test*",top_level_dir=None)
    print(dicover)
    return dicover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    rephtml = os.path.join(os.getcwd(),"report","test.html")
    fp = open(rephtml,"wb")
    runner = HTMLTestRunner(stream=fp,title = u"link interface test report",description = u"用例执行情况：")
    runner.run(all_case())
    fp.close()

