#! /usr/bin/python
# -*-coding:utf-8 -*-
import unittest
import HTMLTestRunner
def baogao():
# def baogao(name):
    suit = unittest.TestSuite()
    # qwe 是请求中的类
    # suit.addTest(unittest.makeSuite(qwe))
    # 两个参数 一个路径 一个参数（通配符）
    dis = unittest.defaultTestLoader.discover(r'D:\Users\ROOM\PycharmProjects\untitled\jieku_kuang\test',pattern='test_*.py')
    for i in dis:
        suit.addTest(i)
    # for i in name:
    #     dis = unittest.defaultTestLoader.discover(r'D:\zls\jiekou_test\jiekou_test',
    #                                               pattern='test_{}.py'.format(i.strip()))
    #     for j in dis:
    #         suit.addTest(j)
    f = open('a.html','wb')
    # 定义一个测试报告信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告',
                                               tester='缪永生',description='结果如下',
                                               )
    #suit是测试套件变量
    runner.run(suit)
    f.close()
baogao()
