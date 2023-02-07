# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-02-03
# @Author  : white
# @FileName: demo.py
# @Software: PyCharm
# **************************************
import requests
import execjs

def get_data():
    url = "https://vipapi.qimingpian.cn/DataList/productListVip"

    params = {
        "time_interval": "",
        "tag": "",
        "tag_type": "",
        "province": "",
        "lunci": "",
        "page": "1",
        "num": "20",
        "unionid": ""
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "69",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "vipapi.qimingpian.cn",
        "Origin": "https://www.qimingpian.com",
        "Pragma": "no-cache",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    res = requests.post(url=url, headers=headers, data=params)
    data = execjs.compile(open('decrypt.js').read()).call('white', res.json())
    print(data)
get_data()
