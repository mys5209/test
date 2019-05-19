#! /usr/bin/python
# -*-coding:utf-8 -*-
from jieku_kuang.report.baogao import baogao
f = open('a.txt','w',encoding='utf-8')
a = f.readlines()
if 'all' == a:
    baogao('*')
else:
    baogao(bb)