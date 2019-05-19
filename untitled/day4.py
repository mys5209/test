#! /usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=30&pagenum=2&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.20955|34.75591|114.560476|34.848733&keywords=%E6%B4%97%E6%B5%B4%E4%B8%AD%E5%BF%83'
res=requests.get(url)
qwe=res.text
asd=json.loads(qwe)
# 将json格式转换成字典
# qwe=json.dumps(asd)
# 将字典转换成json格式
a=(asd['data']['poi_list'][9]['name'])


