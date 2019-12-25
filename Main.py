#coding=utf-8
import unittest
from demo.HTMLTestRunner import HTMLTestRunner
from unittestdemo.test_MyddtTest import myddttest
import os
import sys
basedir=os.path.dirname(os.path.abspath(__file__))
report_path= os.path.join(basedir,"report","result.html")
file_path=os.path.join(basedir,"unittestdemo")
print(file_path,report_path)
#filepath=r'C:\Users\Administrator\PycharmProjects\test\unittestdemo'
rule='test_*.py'

#suite = unittest.TestSuite()
#suite.addTest(myddttest("test_01"))
discover = unittest.defaultTestLoader.discover(start_dir=file_path,pattern=rule)
fp=open(report_path,"wb")
runner = HTMLTestRunner(stream=fp,title="自动化测试报告",description="案例执行",retry=1)
runner.run(discover)
#runner.run(suite)
fp.close()