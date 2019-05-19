#! /usr/bin/python
# -*-coding:utf-8 -*-
from time import sleep
from appium import webdriver
import unittest
class DS(unittest.TestCase):
    d = {
        "device": "android",
        "platformName": "Android",
        "platfromVersion": "8.1.0",
        "deviceName": "SSIR6SHYDIVS7P8T",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    @classmethod
    def setUpClass(cls):
        cls.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=cls.d)
        sleep(10)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def test_1(self):
        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'QQ')
        sleep(10)
    def test_2(self):
        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'微信')
        sleep(10)
    def test_3(self):
        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'密码')
        sleep(10)
    def test_4(self):
        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'微博')
        sleep(10)
if __name__=='__main__':
        unittest.main()