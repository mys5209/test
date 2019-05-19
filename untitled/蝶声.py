#! /usr/bin/python
# -*-coding:utf-8 -*-
#第一步导入appium模块中的webdriver类
from appium import webdriver
from time import sleep
#面向过程
#测试脚本与服务器进行连接的参数数据
# d={
#       "device": "android",
#       "platformName": "Android",
#       "platfromVersion": "8.1.0",
#       "deviceName": "SSIR6SHYDIVS7P8T",
#       "appPackage": "com.qk.butterfly",
#       "appActivity": ".main.LauncherActivity",
#       "noReset": "True"
#   }
#写死的http:123.0.0.1:4723/wb/hub
#测试脚本是appium服务器与手机建立连接的过程
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(10)
#元素是id,就使用id定位方式
#dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
#插入等待时间,休眠几秒
#获取微信的文字
#元素的多级定位
#先定义上一级在定位下面的元素没有id找class
#send_keys()输入的是字符串
#什么时候可以用send_keys?
#像手机的输入框内输入数据的时候
#clickable-->>true
#enable-->>true
#foucsable-->>>true
#text=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# from appium import webdriver
# from time import sleep
# d={
#       "device": "android",
#       "platformName": "Android",
#       "platfromVersion": "8.1.0",
#       "deviceName": "SSIR6SHYDIVS7P8T",
#       "appPackage": "com.qk.butterfly",
#       "appActivity": ".main.LauncherActivity",
#       "noReset": "True"
#   }
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15225453394')
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('mysmys5209')
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(5.0)
# #退出app包括后台进程也关掉
# #dr.quit()
# from time import sleep
# from appium import webdriver
# d={
#       "device": "android",
#       "platformName": "Android",
#       "platfromVersion": "8.1.0",
#       "deviceName": "SSIR6SHYDIVS7P8T",
#       "appPackage": "com.qk.butterfly",
#       "appActivity": ".main.LauncherActivity",
#       "noReset": "True"
#   }
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15225453394')
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('mysmys5209')
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(10)
# dr.quit()
from time import sleep
from appium import webdriver
d={
      "device": "android",
      "platformName": "Android",
      "platfromVersion": "8.1.0",
      "deviceName": "SSIR6SHYDIVS7P8T",
      "appPackage": "com.qk.butterfly",
      "appActivity": ".main.LauncherActivity",
      "noReset": "True"
  }
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15225453394')
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('mysmys5209')
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

