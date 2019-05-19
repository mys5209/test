#! /usr/bin/python
# -*-coding:utf-8 -*-
# from time import sleep
# from appium import webdriver
# import unittest
# d={
#       "device": "android",
#       "platformName": "Android",
#       "platfromVersion": "8.1.0",
#       "deviceName": "SSIR6SHYDIVS7P8T",
#       "appPackage": "com.qk.butterfly",
#       "appActivity": ".main.LauncherActivity",
#       "noReset": "True"
#     }
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(4)
# # text=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').click()
# # text=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# # print(text)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15225453394')
# #清空数据
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('mysmys5209')
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(5.0)
# # #dr.quit()
# #app退出登录
# # def logout(self):
#       #find_element_by_class_name()定义一个class属性的元素，要求该元素唯一
#       #find_elements_by_class_name()定位多个class属性的元素，元素是多个
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# print(a)
# #可点击操作  返回值列表
# a[3].click()
# sleep(5)
# # if __name__=='__main__':
# #        unittest.main()
#       # logout()
# #前提设置没有出现在屏幕上的情况
# #模拟人工上滑获取当前屏幕分辨率
# # size = dr.get_window_size()
# # x1 = size['width'] * 0.5  # x坐标 50
# # y1 = size['height'] * 0.25  # 起始y坐标 50
# # y2 = size['height'] * 0.75  # 150
# # for i in range(2):
# #     dr.swipe(
# # )
# #seipe滑动自带的函数
# dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/v_set_out').click()
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
# sleep(5)
#
#

from time import sleep
from appium import webdriver


class DS(object):

    d = {
        "device": "android",
        "platformName": "Android",
        "platfromVersion": "8.1.0",
        "deviceName": "SSIR6SHYDIVS7P8T",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

    def __init__(self):
        self.d = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
        sleep(10)

    def check_text(self):
        text = self.d.find_element_by_id('com.qk.butterfly:id/v_login_wx').\
            find_element_by_class_name('android.widget.TextView').text
        print(text)
        sleep(5)
        return text

    def check_text1(self):
        text1 = self.d.find_element_by_id('com.qk.butterfly:id/v_login_qq').\
            find_element_by_class_name('android.widget.TextView').text
        print(text1)
        sleep(5)
        return text1

    def check_text2(self):
        text2 = self.d.find_element_by_id('com.qk.butterfly:id/v_login_wb').\
            find_element_by_class_name('android.widget.TextView').text
        print(text2)
        sleep(5)
        return text2

    def check_text3(self):
        text3 = self.d.find_element_by_id('com.qk.butterfly:id/v_login_pwd').\
            find_element_by_class_name('android.widget.TextView').text
        print(text3)
        sleep(5)
        return text3

    def close_app(self):
        self.d.quit()


if __name__ == '__main__':

    so = DS()
    so.check_text()
    so.check_text1()
    so.check_text2()
    so.check_text3()
    so.close_app()

#
# from time import sleep
# from appium import webdriver
# import unittest
# class DS(unittest.TestCase):
#
#
#
#     d={
#         "device": "android",
#         "platformName": "Android",
#         "platfromVersion": "8.1.0",
#         "deviceName": "SSIR6SHYDIVS7P8T",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#         }
#
#
#
#
#     @classmethod
#     def setUpclass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
#         sleep(5)
#
#
#     @classmethod
#     def tearDownclass(cls):
#         cls.dr.quit()
#
#
#
#     def test_1(self):
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').\
#             find_elements_by_class_name('android.widget.TextView').text
#         print(text)
#         self.assertEqual(text,'微信')
#
#
# if __name__=='__main__':
#
#      unittest.main()
#
