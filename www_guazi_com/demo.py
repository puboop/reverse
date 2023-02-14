# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-02-03
# @Author  : white
# @FileName: demo.py
# @Software: PyCharm
# **************************************
import base64
import requests
import time
import hashlib
import execjs
import re

url = "https://mapi.guazi.com/car-source/carList/pcList"
params = {
    "versionId": "0.0.0.0",
    "sourceFrom": "wap",
    # "deviceId": "22cc0a35-c331-4520-9359-a2f00e4cf22d",
    "deviceId": "",
    "osv": "Windows 10",
    "minor": "",
    "sourceType": "",
    "ec_buy_car_list_ab": "",
    "location_city": "",
    "district_id": "",
    "tag": "-1",
    "license_date": "",
    "auto_type": "",
    "driving_type": "",
    "gearbox": "",
    "road_haul": "",
    "air_displacement": "",
    "emission": "",
    "car_color": "",
    "guobie": "",
    "bright_spot_config": "",
    "seat": "",
    "fuel_type": "",
    "order": "",
    "priceRange": "0,-1",
    "tag_types": "",
    "diff_city": "",
    "intention_options": "",
    "initialPriceRange": "",
    "monthlyPriceRange": "",
    "transfer_num": "",
    "car_year": "",
    "carid_qigangshu": "",
    "carid_jinqixingshi": "",
    "cheliangjibie": "",
    "page": "1",
    "pageSize": "20",
    "city_filter": "12",
    "city": "12",
    "guazi_city": "12",
    "qpres": "",
    "platfromSource": "wap"
}
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
    # "anti-token": "1277105907",
    "anti-token": "",
    "cache-control": "no-cache",
    "client-time": "1676339048",
    "client-timestamp": "1676339047",
    "origin": "https://www.guazi.com",
    "platform": "5",
    "pragma": "no-cache",
    "referer": "https://www.guazi.com/",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    # "szlm-id": "D2TApCweUFjrkox8bhPeLjfCnLiV1rN6j8LXcArwhoJ/8X56",
    "token": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    # "verify-token": "5f808328357bfadc881711e9240e1f87"
}
cookies = {
    # "uuid": "22cc0a35-c331-4520-9359-a2f00e4cf22d",
    # "sessionid": "0f50d688-df8c-4ea3-e4ba-ba5b1e115753",
    # "guazitrackersessioncadata": "%7B%22ca_kw%22%3A%22-%22%7D",
    # "cainfo": "%7B%22ca_s%22%3A%22seo_bing%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%2222cc0a35-c331-4520-9359-a2f00e4cf22d%22%7D"
}
res = requests.get(url=url, headers=headers, cookies=cookies, params=params)
data = res.text
map_data = {"&#59854;": 0,
            "&#59246;": 1,
            "&#57808;": 2,
            "&#60146;": 3,
            "&#59537;": 4,
            "&#58149;": 5,
            "&#58397;": 6,
            "&#58670;": 7,
            "&#58928;": 8,
            "&#60492;": 9, }
# 替换处理
for _k, _v in map_data.items():
    data = data.replace(_k, str(_v))
data = eval(data)
for _i in data['data']['postList']:
    print(_i)
