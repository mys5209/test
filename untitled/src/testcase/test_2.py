#! /usr/bin/python
# -*-coding:utf-8 -*-
#导入函数
from src.func.func_2 import wx,qq,wb,mm
from appium import webdriver
import unittest
import HTMLTestRunner
from time import sleep
from  src.until.logs import get_logger

# from src.until.logs import mulu
#给日志一个变量g g是全局变量
g=get_logger(name='test_2.py')
#测试脚本
class Text(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
            d = {
                  "device": "android",
                  "platformName": "Android",
                  "platfromVersion": "8.1.0",
                  "deviceName": "SSIR6SHYDIVS7P8T",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity",
                  "noReset": "True"
            }
            cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
            sleep(10)
            g.info('APP建立连接完成')


      @classmethod
      def tearDownClass(cls):
            cls.dr.quit()
            sleep(10)
            g.info('app关闭')
          #测试用例的代码
      def test_1(self):
            g.info('执行测试用例')
            #验证微信的用例
            text=wx(self.dr)
            #断言
            self.assertEquals(text,'微信')
            sleep(10)
      def test_2(self):
            g.info('执行测试用例')
            text=qq(self.dr)
            self.assertEqual(text,'QQ')
            sleep(10)
      def test_3(self):
            g.info('执行测试用例')
            text=wb(self.dr)
            self.assertEqual(text,'微博')
            sleep(10)
      def test_4(self):
            g.info('执行测试用例')
            text=mm(self.dr)
            self.assertEqual(text,'密码')
            sleep(10)
      #运行测试脚本生成测试报告
if __name__=='__main__':
      #创建测试套件
      suite=unittest.TestSuite()
      suite.addTest(Text('test_1'))
      suite.addTest(Text('test_2'))
      suite.addTest(Text('test_3'))
      suite.addTest(Text('test_4'))
       #将路径写死
      # r_path=''uses/////'
      # #将路径写活
      # r_path_1=REPORT_DIR'HTMLReport.html'
      with open(r'D:\Users\ROOM\PycharmProjects\untitled\src\testcase\jieguo.html','wb') as fb:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='接口测试报告', tester='缪永昇', description='结果如下',verbosity=2)
            runner.run(suite)

