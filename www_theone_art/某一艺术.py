# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-07
# @Author  : white
# @FileName: 某一艺术.py
# @Software: PyCharm
# **************************************
import requests
import execjs
from urllib.parse import quote

cookies = dict()

def get_encrypt():
    '''
    1、发起第一次请求获取加密数据，然后解密；
    2、解密获取sig的加密参数；
    3、加密获取到的参数
    4、发送请求获取最终数据
    '''
    url = "https://api.theone.art/market/api/key/get"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    return execjs.compile(open('sig.js', encoding="utf-8").read()).call("tripleAesDecrypt", res.json()["data"])


def get_data():
    sig = get_encrypt()
    url = 'https://api.theone.art/market/api/saleRecord/list/v2'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "api.theone.art",
        "Origin": "https://www.theone.art",
        "Referer": "https://www.theone.art/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sig": quote(sig),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    data = {
        "authorId": None,
        "chainContract": None,
        "commodityCategoryId": None,
        "commodityCategoryIdList": [],
        "commodityId": None,
        "highPrice": "",
        "lowPrice": "",
        "pageCount": 1,
        "pageSize": 20,
        "seriesWorks": None,
        "seriesWorksId": None,
        "sort": {"field": 2, "upOrDown": 1},
        "statusSell": 1,
        "topicId": None,
        "typeMarket": 1,
        "commodityTraitList": [],
        "sig": sig
    }

    res = requests.post(url=url, headers=headers, json=data)
    print(res.text)


get_data()
