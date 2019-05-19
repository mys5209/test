#! /usr/bin/python
# -*-coding:utf-8 -*-
import os
#获取当前文件夹所在的位置的绝对路径
a=os.path.dirname(os.path.abspath(__file__))
print(a)

#项目根目录
b=BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(b)
#  日志目录
c=LOG_DIR=BASE_DIR+'/logs/'
print(c)
#报告目录
REPORT_DIR=BASE_DIR+'report'
#源文件目录
SRC_DIR=BASE_DIR+'/src/'
#测试用目录
TEST_CASE=BASE_DIR+'/testcase/'
#页面方法目录
FUNC=BASE_DIR+'/func/'
#公共目录
UNTIL=BASE_DIR+'/until/'