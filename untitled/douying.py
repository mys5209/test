#! /usr/bin/python
# -*-coding:utf-8 -*-
from time import sleep
from appium import webdriver

# a= {
#       "device": "android",
#       "platformName": "Android",
#       "platfromVersion": "8.1.0",
#       "deviceName": "SSIR6SHYDIVS7P8T",
#       "appPackage": "com.ss.android.ugc.aweme",
#       "appActivity": ".main.MainActivity",
#       "noReset": "True"
#     }
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=a)
# sleep(5)
# a=dr.find_element_by_id('com.ss.android.ugc.aweme:id/kq').find_elements_by_class_name('android.widget.FrameLayout')
# a[4].click()
# dr.find_element_by_id('手机验证码或密码登录').click()
# sleep(5)
# dr.find_element_by_id('com.ss.android.ugc.aweme:id/aqd').click()
# sleep(5)
# dr.find_element_by_id('com.ss.android.ugc.aweme:id/am9').send_keys('15225453394')
# sleep(5)
# dr.find_element_by_id('com.ss.android.ugc.aweme:id/aqb').send_keys('mysmys5209')
# sleep(5)
# dr.find_element_by_id('com.ss.android.ugc.aweme:id/ly').click()
# sleep(5)
# size = dr.get_window_size()
# x1 = size['width'] * 0.5
# y1 = size['height'] * 0.25
# y2 = size['height'] * 0.75
# for i in range(4):
#     dr.swipe(x1,y2,x1,y1)
#     sleep(20)

#selenium
from selenium import webdriver
import time
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']
#定义要打开的浏览器
dr = webdriver.Firefox()
#请求网页
dr.get('http://www.baidu.com')
time.sleep(2)
#关闭浏览器
dr.quit()


