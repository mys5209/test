#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
import warnings

class DieS(unittest.TestCase):

	d ={
  		"device": "android",
  		"platformName": "Android",
  		"platfromVersion": "9",
  		"deviceName": "30b78ff2",
  		"appPackage": "com.qk.butterfly",
  		"appActivity": ".main.LauncherActivity",
  		"noReset": "True"
		}
	@classmethod
	def setUpClass(cls):
		# 忽略报警
		warnings.simplefilter('ignore',ResourceWarning)
		cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=cls.d)
		sleep(10)

	# def test_check_wx_text(self):
	# 	text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
	# 	self.assertEqual(text,'微信')

	# def test_check_qq_text(self):
	# 	text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
	# 	self.assertEqual(text,'QQ')

	# def test_check_wb_text(self):
	# 	text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
	# 	self.assertEqual(text,'微博')

	# def test_check_ma_text(self):
	# 	text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
	# 	self.assertEqual(text,'密码')
	def tiao_zhuan(self):
		self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
		sleep(5)


@classmethod


def tearDownClass(cls):
    sleep(2)
    cls.dr.quit()


if __name__ == '__main__':
    dd = DieS()
    dd.setUpClass()
    dd.login('15225453394', 'mysmys5209')
    dd.tearDownClass()

