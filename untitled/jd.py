#! /usr/bin/python
# -*-coding:utf-8 -*-
from time import sleep
from selenium import webdriver


class JD(object):

    def __init__(self):
        self.dr = webdriver.Firefox()
        sleep(10)

    def qq(self):
        aa = self.dr.get('https://www.douban.com')
        sleep(10)


    def tex(self):
        bb = self.dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
        sleep(10)


    def tupian(self):
        cc = self.dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[1]/a').click()
        sleep(10)


# def sb(self):
# 	self.dr.quit()


if __name__ == '__main__':

    go = JD()
    go.qq()
    go.tex()
    go.tupian()