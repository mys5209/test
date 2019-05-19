#! /usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
import pymysql
import re
import xlrd
import xlwt
class zhilian(object ):
    def ack(self,page):
        url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.30495411&x-zp-page-request-id=561d9bf77cd34cd78245b1a6406bc39c-1554017141936-234140'.format(page*90)
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        res = requests .get(url,headers = head)
        xhr = res.content .decode('utf-8')
        print(xhr)
        return xhr
    # def gulv(self,abc):
    #     asd = json.loads(abc)
    #     a, b, c, d, e, f, g = [], [], [], [], [], [], []
    #     for i in range(90):
    #         uptime = asd['data']['results'][i]['updateDate']
    #         a.append(uptime)
    #         city = asd['data']['results'][i]['city']['display']
    #         b.append(city)
    #         salary = asd['data']['results'][i]['salary']
    #         c.append(salary)
    #         name = asd['data']['results'][i]['company']['name']
    #         d.append(name)
    #         jobname = asd['data']['results'][i]['jobName']
    #         e.append(jobname)
    #         edulevel = asd['data']['results'][i]['eduLevel']['name']
    #         f.append(edulevel)
    #         workingexp = asd['data']['results'][i]['workingExp']['name']
    #         g.append(workingexp)
    #     abc = list(zip(d, b, c, a, e, f, g))
    #     return abc


# def xls(self, abc):
#     f = xlwt.Workbook(encoding='utf-8')
#     sheet = f.add_sheet('zhilian')
#     for i in range(len(abc)):
#         sheet.write(i, 0, abc[i][0])
#         sheet.write(i, 1, abc[i][1])
#         sheet.write(i, 2, abc[i][2])
#         sheet.write(i, 3, abc[i][3])
#         sheet.write(i, 4, abc[i][4])
#         sheet.write(i, 5, abc[i][5])
#         sheet.write(i, 6, abc[i][6])
#     f.save('b.xls')
#
#
# def shuju(self, abc):
#     conn = pymysql.connect(
#         host='192.168.2.206',
#         port=3306,
#         user='root',
#         passwd='123456')
#     asd = conn.cursor()
#     asd.execute('use wang;')
#     asd.execute(
#         'create table dianying(公司名称 char(255),工作地址 char(255),薪资 char(255),发布时间 char(255),职务 char(255),学历 char(255),工作经验 char(255));')
#     for i in range(len(abc)):
#         asd.execute(
#             'insert into dianying values("{}","{}","{}","{}","{}","{}","{}");'.format(abc[i][0], abc[i][1], abc[i][2],
#                                                                                       abc[i][3], abc[i][4], a
zhilian()
tt=zhilian.ack(1)
try:
    f = xlrd.open_workbook('aaa.xls')
    read = f.sheets()[0]
    hang = read.nrows
    new_f = copy(f)
    new_sheet = new_f.get_sheet(0)
    z2 = hang + 1
    for a, b, c, d, e, f, g in ABC:
        new_sheet.write(z2, 0, a)
        new_sheet.write(z2, 1, b)
        new_sheet.write(z2, 2, c)
        new_sheet.write(z2, 3, d)
        new_sheet.write(z2, 4, e)
        new_sheet.write(z2, 5, f)
        z2 += 1
    new_f.save('aaa.xls')
except:
    ff = xlwt.Workbook(encoding='utf-8')
    sheet = ff.add_sheet('sheet1')
    sheet.write(0, 0, '薪资')
    sheet.write(0, 1, '地点')
    sheet.write(0, 2, '名字')
    sheet.write(0, 3, '岗位')
    sheet.write(0, 4, '经验')
    sheet.write(0, 5, '时间')
    sheet.write(0, 6, '学历')
    z1 = 1
    for a, b, c, d, e, f, g in ABC:
        sheet.write(z1, 0, a[0][0])
        sheet.write(z1, 1, b[0][1])
        sheet.write(z1, 2, c[0][2])
        sheet.write(z1, 3, d[0][3])
        sheet.write(z1, 4, e[0][4])
        sheet.wrrite(z1, 5, f[0][5])
        sheet.write(z1, 6, g[0][6])
    ff.save('aaa.xls')