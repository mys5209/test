#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep
class DS(object):
 # 测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "SSIR6SHYDIVS7P8T",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
#账号密码输入函数
    def login(self,phone,password):
        self.tiao_zhuang()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        sleep(10)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(5.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)
    # 建立连接的函数

    def __init__(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(10.0)
    #跳转到手机号密码登录页面的函数
    def tiao_zhuang(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(10)

    # 检查那四个文字的函数/方法
    # def check_text(self):
    #
    #     # 获取微信文字
    #     text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
    #
    #     return text


# app退出登录
    def logout(self):
    # find_element_by_class_name()定义一个class属性的元素，要求该元素唯一
    # find_element_by_class_name()定位多个class属性的元素，元素是多个
        a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        print(a)
    # 关闭app的函数
    # def close_app(self):
    #     self.dr.quit()
if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go
    # 调用DS类的方法
    go.login('15225453394','mysmys5209')
    # go.close_app()
    go.tiao_zhuang()
    go.logout()