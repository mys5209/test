#! /usr/bin/python
# -*-coding:utf-8 -*-
import os
import logging
import datetime
#创建一个日志文件的名字
logs=os.path.join(r'D:\Users\ROOM\PycharmProjects\untitled\src\logs',
                  str(datetime.datetime.now().date())+'.out')
print(logs)
#创建一个日志的输出格式
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
#日志输出的控制台
con_handler= logging.StreamHandler()
#加载日志格式
con_handler.setFormatter(formatter)
#将日志输出到文本
fil_handler = logging.FileHandler(logs,encoding='utf-8')
#加载日志格式
fil_handler.setFormatter(formatter)
#定义一个函数
def get_logger(name):
    #获取文件名字传入日志中
     logger=logging.getLogger(name)
     #加入一个手柄
     logger.addHandler(con_handler)
     logger.addHandler(fil_handler)
      #设置日志脚本
     logger.setLevel(logging.INFO)

     return logger
go=get_logger('logs.py')
go.info('hahaha')