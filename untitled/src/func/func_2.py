#! /usr/bin/python
# -*-coding:utf-8 -*-
import yaml
from time import sleep
with open(r'D:\Users\ROOM\PycharmProjects\untitled\src\element\item.yaml', 'r', encoding='utf-8') as fb:
    # item=yaml.load(fb)使用yaml模块的load方法将yaml文件中的数据转换成python字典格式的形式
    item_data=yaml.load(fb,Loader=yaml.CFullLoader)
    # print(item_data)
    # print(type(item_data))
    # print(item_data['three']['wx_id'])


def wx(driver):
    text = driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def qq(driver):
    text = driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def wb(driver):
    text = driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def mm(driver):
    text = driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    return text