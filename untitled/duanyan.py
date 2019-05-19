#! /usr/bin/python
# -*-coding:utf-8 -*-
#面向对象
from appium import webdriver
from time import sleep
import unittest
class DS(unittest.TestCase):
   #测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platfromVersion": "8.1.0",
        "deviceName": "SSIR6SHYDIVS7P8T",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
   #初始化测试环境的方法/函数
   #断言微信文字是否存在

    # def setUp(self):
    # self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
    #     sleep(5)
        #检查那四个文字的函数/方法
    # def test_1(self):
    #     text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        #断言
        # self.assertEqual(text,'QQ')
       #所有的用例执行完毕，跑一次，就跑一次
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
        sleep(10)
    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.dr.quit()

    def test_1(self):
         text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
         self.assertEqual(text,'QQ')
         sleep(2)
    def test_2(self):
        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'微信')
        sleep(2)
    def test_3(self):
        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'密码')
        sleep(2)
    def test_4(self):
        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'微博')
        sleep(2)
       #清理测试环境
    # def tearDown(self):
    #     sleep(3)
    #     self.dr.quit()
    # def close_app(self):
    #     sleep(2)
    #     self.dr.quit()
if __name__=='__main__':
       # go=DS() #创建一个ds的类实例，赋给变量go
    #调用ds类的方法
       # go.check_test()
       # go.close_app()
       unittest.main()
       #verbosity=2,warnings=True 使输出更详细

