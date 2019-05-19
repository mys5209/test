#! /usr/bin/python
# -*-coding:utf-8 -*-
# import requests
# from jieku_kuang.data.du
# class deng():
#     def get(self,user,password):
#         url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#         payload = '{"phone":%d,"password":%d,"zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"}'%(user,password)
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'User-Agent': "PostmanRuntime/7.11.0",
#             'Accept': "*/*",
#             'Cache-Control': "no-cache",
#             'Postman-Token': "4ebd910a-4324-439a-bec4-dba1c2e6dc33,ada77b3f-fe18-454c-a9fe-799976dcfbf8",
#             'Host': "120.132.8.33:9000",
#             'accept-encoding': "gzip, deflate",
#             'content-length': "152",
#             'Connection': "keep-alive",
#             'cache-control': "no-cache"
#             }
#         response = requests.request("POST", url, data=payload, headers=headers)
#         res = response.json()
#         return res
# if __name__ == '__main__':
#     shuju = denglu().data()
#     print(shuju)
#     for i in range(len(shuju)):
#         a = deng().get(shuju[i][0],shuju[i][1])
#         # print(a)
import requests
from jieku_kuang.data.duqu import Shuju
class qingqiu():
    def denglu(self,user,passwd):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = '{"phone":"%s","password":"%s","zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"}' % (
            user, passwd)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'cache-control': "no-cache"
        }
        response = requests.post(url, data=payload, headers=headers)
        res=response.json()
        return res
if __name__ == '__main__':
    shu=Shuju().shuju()
    for i in range(len(shu)):
        aa=qingqiu().denglu(int(shu[i][0]),int(shu[i][1]))
        print(aa)

