#! /usr/bin/python
# -*-coding:utf-8 -*-
# import pymysql
from xlutils.copy import copy
import xlrd
import xlwt
import requests
import re
import json
import pymysql
class mys(object):
    def qq(self,page):
        url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.26994542&x-zp-page-request-id=09ff973f38f84822a0afcc38ceb8adbf-1554175803114-438194'.format(page*90)
        head ={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/70.0.3538.110 Safari/537.36'}
        res=requests.get(url,headers=head)
        qwe=res.content.decode('utf-8')
        return qwe
    def gl(self,abc):
        asd = json.loads(abc)
        a,b,c,d,e,f,g=[],[],[],[],[],[],[]
        for j in range(len(asd['data']['results'])):
            salary=asd['data']['results'][j]['salary']
            a.append(salary)
            local=asd['data']['results'][j]['city']['display']
            b.append(local)
            name=asd['data']['results'][j]['company']['name']
            c.append(name)
            gangwei=asd['data']['results'][j]['jobType']['display']
            d.append(gangwei)
            we=asd['data']['results'][j]['workingExp']['name']
            e.append(we)
            date=asd['data']['results'][j]['updateDate']
            f.append(date)
            xl=asd['data']['results'][j]['eduLevel']['name']
            g.append(xl)
        ABC=list(zip(a,b,c,d,e,f,g))
        return ABC
    def ro(self,ABC):
        try:
            mm=xlrd.open_workbook('yyy.xls')
            new_mm=copy(mm)
            sh=new_mm.sheets()[0]
            h=sh.nrows
            z=h+2
            for i in range(1,5):
                for j in range(len(ABC)):
                    sh.write(z+j, 0, ABC[j][0])
                    sh.write(z+j, 1, ABC[j][1])
                    sh.write(z+j, 2, ABC[j][2])
                    sh.write(z+j, 3, ABC[j][3])
                    sh.write(z+j, 4, ABC[j][4])
                    sh.write(z+j, 5, ABC[j][5])
                    sh.write(z+j, 6, ABC[j][6])
            new_mm.save('yyy.xls')
        except:
            ff= xlwt.Workbook(encoding='utf-8')
            sheet=ff.add_sheet('zhilian')
            sheet.write(0, 0, '薪资')
            sheet.write(0, 1, '地区')
            sheet.write(0, 2, '名字')
            sheet.write(0, 3, '职位')
            sheet.write(0, 4, '经验')
            sheet.write(0, 5, '时间')
            sheet.write(0, 6, '学历')
            for k in range(len(ABC)):
                sheet.write(k+1, 0, ABC[k][0])
                sheet.write(k+1, 1, ABC[k][1])
                sheet.write(k+1, 2, ABC[k][2])
                sheet.write(k+1, 3, ABC[k][3])
                sheet.write(k+1, 4, ABC[k][4])
                sheet.write(k+1, 5, ABC[k][5])
                sheet.write(k+1, 6, ABC[k][6])
                ff.save('yyy.xls')



    #  # def shuju(self, hahaha):
    #     conn = pymysql.connect(
    #         host='192.168.1.19',
    #         port=3306,
    #         user='root',
    #         passwd='123456')
    #     asd = conn.cursor()
    #     asd.execute('use mys;')
    #     asd.execute('create table hehehe(名字 char(255),地方 char(255),薪资 char(255),发布时间 char(255),职务 char(255),学历 char(255),工作经验 char(255));')
    #     for j in range(len(hahaha)):
    #         asd.execute('insert into hehehe values("{}","{}","{}","{}","{}","{}","{}");'.format(abc[i][0], abc[i][1],
    #                                                                                       abc[i][2],
    # def shuju(self,abc):
    #        conn=pymysql.connect(host='192.168.1.11',port=3306,user='root',passwd='123456')
    #        mys=conn.cursor()
    #    # mys.execute('create database yinyu;')
    #        mys.execute('use yinyu;')
    #        try:
    #            mys.execute('create table ruanji(薪水 char(255),地点 char(255),名字 char(255),岗位 char(255),经验 char(255),发布日期 char(255),学历 char(255));')
    #            for k in range(len(abc)):
    #             mys.execute('insert into ruanji values("{}","{}","{}","{}","{}","{}","{}");'.format(abc[k][0],abc[k][1],abc[k][2],abc[k][3],abc[k][4],abc[k][5],abc[k][6]))
    #        except:
    #         for k in range(len(abc)):
    #             mys.execute('insert into ruanji values("{}","{}","{}","{}","{}","{}","{}");'.format(abc[k][0], abc[k][1], abc[k][2],
    #                                                                               abc[k][3], abc[k][4], abc[k][5],
    #                                                                               abc[k][6]))
dp = mys ()
for i in range(5):
    abc=dp.qq(i)
    ABC=dp.gl(abc)
    ppp=dp.ro(ABC)
    # dp.save(ppp)




















