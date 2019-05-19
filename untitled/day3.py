#! /usr/bin/python
# -*-coding:utf-8 -*-
import re
import requests
from xlutils.copy import copy
import xlrd
import xlwt
class doupan(object):
    def zz(self,page):
        url='https://movie.douban.com/top250?start={}&filter='.format(page)
        head={'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv:66.0)Gecko/20100101 Firefox/66.0'
            }
        res=requests.get(url,headers=head)
        haha=res.content.decode('utf-8')
        return haha
    def gl(self,abc):
        pj=[]
        pianming=re.compile(r'<img width="100" alt="(.*?)"',re.S)
        pianming1=pianming.findall(abc)
        zongjie=re.compile(r'<span class="inq">(.*?)。',re.S)
        zongjie1=zongjie.findall(abc)
        daoyan=re.compile(r'导演:(.*?);',re.S)
        daoyan1=daoyan.findall(abc)
        pingfen=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>',re.S)
        pingfen1=pingfen.findall(abc)
        pingjia = re.compile(r'<div class="star">(.*?)</div>', re.S)
        pingjia1 = pingjia.findall(abc)
        for i in pingjia1:
            new_p = re.compile(r'<span>(.*?)</span>', re.S)
            aaa = new_p.findall(i)
            pj.extend(aaa)
        # return \
        print(list(zip(pianming1,daoyan1,pingfen1,pj)))

    def save(self,list):
       try:
           f=xlrd.open_workbook('aaa.xls')
           read=f.sheets()[0]
           hang=read.nrows
           new_f=copy(f)
           new_sheet=new_f.get_sheet(0)
           z2=hang+1
           for q,w,e,r in list:
               new_sheet.write(z2, 0, q)
               new_sheet.write(z2, 1, w)
               new_sheet.write(z2, 2, e)
               new_sheet.write(z2, 3, r)
               z2+=1
           new_f.save('aaa.xls')
       except:
            ff=xlwt.Workbook(encoding='utf-8')
            sheet=ff.add_sheet('sheet1')
            sheet.write(0,0,'电影名')
            sheet.write(0,1,'导演')
            sheet.write(0,2,'评分')
            sheet.write(0,3,'评价')
            z1=1
            for q, w, e, r in list:
                sheet.write(z1, 0, q)
                sheet.write(z1, 1, w)
                sheet.write(z1, 2, e)
                sheet.write(z1, 3, r)
                z1+=1
            # ff.save('aaa.xls')

m=doupan()
for page in range(1,6):
    abc=m.zz(page)
    sh=m.gl(abc)
    # m.save(sh)

