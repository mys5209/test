#! /usr/bin/python
# -*-coding:utf-8 -*-
#服务器
# import socket
#
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.1.10',45))
# while True:
#     #第一个参数客户端的请求数据
#     #第二个参数客户端的ip和端口号
#     client,addr=s.recvfrom(1024)
#     print(client)
#     print(client.decode('utf-8'))
#     msg='hello'
#     s.sendto(msg.encode('utf-8'),addr)
#
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('hahaha')
# f.save('mm.xls')
from time import sleep
from appium import webdriver
import unittest
class DS(unittest.TestCase):

 d = {
         "device": "android",
         "platformName": "Android",
         "platformVersion": "6.0.1",
         "deviceName": "3493f5137d5",
         "appPackage": "com.qk.butterfly",
         "appActivity": ".main.LauncherActivity",
         "noReset": "True"
    }

    @classmethod
    def setUpclass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(5)


    @classmethod
    def tearDownclass(cls):
     cls.dr.quit()


    def test_1(self):
     text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').\
    	find_element_by_class_name('android.widget.TextView').text
     print(text)
     self.assertEqual(text,'微信')


if __name__=='__main__':
    unittest.main()