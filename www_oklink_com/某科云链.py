# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-09
# @Author  : white
# @FileName: 某科云链.py
# @Software: PyCharm
# **************************************
import requests
import execjs
import time


def get_data():
    url = 'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict'
    headers = {
        "Host": "www.oklink.com",
        "Referer": "https://www.oklink.com/zh-cn/btc/tx-list?limit=20&pageNum=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-apiKey": execjs.compile(open('x-apiKey.js', encoding='utf-8').read()).call("white"),
        "x-cdn": "https://static.oklink.com",
    }
    data = {
        "t": str(int(time.time() * 1000)),
        "limit": "20",
        "offset": "0"
    }
    res = requests.get(url=url, headers=headers).json()["data"]
    for room in res['hits']:
        house = dict()
        house['交易哈希'] = room['hash']
        house['所在区块'] = room['blockHeight']
        house['输入'] = room['inputsCount']
        house['输出'] = room['outputsCount']
        print(house)


get_data()
