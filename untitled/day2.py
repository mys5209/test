#! /usr/bin/python
# -*-coding:utf-8 -*-
import re
import requests
class dp(object):
    def room(self,b):
        url='https://movie.douban.com/top250?start={}&filter='.format(b)
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
            }
        res=requests.get(url,headers=head)
        mys=res.content.decode('utf-8')
        return mys
    def gl(self,c):
        patt=re.compile(r'<img width="100" alt="(.*?)"',re.S)
        items=patt.findall(c)
        http=re.compile(r'src="(.*?)" class=""')
        item=http.findall(c)
        c=dict(zip(items,item))
        return c
    def save(self,u):
        for i,j in u.items():
            res=requests.get(j)
            mys=res.content
            with open('{}.jpg'.format(i),'wb') as f:
                 f.write(mys)
a=dp()
for i in range(0,125,25):
    c=a.room(i)
    u=a.gl(c)
    a.save(u)








