# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-19
# @Author  : white
# @FileName: login.py
# @Software: PyCharm
# **************************************
import time
import execjs
import requests
import base64
import re

username = "123456789"
password = "000000"

info = dict()

def get_raskey():
    '''pluginSSOController.preloginCallBack({"retcode":0,"servertime":1674130153,"pcid":"gz-47abf2effd10c4387884a3aebde96831a140","nonce":"9603V8","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":3})'''
    url = "https://login.sina.com.cn/sso/prelogin.php"
    params = {
        "entry": "news",
        "callback": "pluginSSOController.preloginCallBack",
        "su": base64.b64encode(username.encode()),
        "rsakt": "mod",
        "checkpin": "1",
        "client": "ssologin.js(v1.4.19)",
        "_": "1674105127491"
    }
    headers = {
        "referer": "https://news.sina.com.cn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers, params=params)
    result = re.findall('"servertime":(\d+),.*?"nonce":"(.*?)","pubkey":"([A-Z0-9]+)","rsakv":"(\d+)"', res.text)
    return {"servertime": result[0][0], "nonce": result[0][1], "rsaPubkey": result[0][2], "rsakv": result[0][3]}

def login():
    '''{'servertime': '1674130719', 'nonce': 'D6ESUP', 'rsaPubkey': 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443', 'rsakv': '1330428213', 'username': '123456789', 'password': '000000'}'''
    info.update(get_raskey())
    info.update({"username": username, "password": password})
    print(info)
    url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=" + str(time.time() * 1000)
    params = {
        "entry": "news",
        "gateway": "1",
        "from": "",
        "savestate": "30",
        "qrcode_flag": "true",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": base64.b64encode(username.encode()),
        "service": "sso",
        "servertime": info["servertime"],
        "nonce": info["nonce"],
        "pwencode": "rsa2",
        "rsakv": info["rsakv"],
        "sp": execjs.compile(open("pwd.js", encoding='utf-8').read()).call("white", info),
        "sr": "1536*864",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "273",
        "returntype": "TEXT"
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "cache-control": "no-cache",
        "content-length": "542",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://news.sina.com.cn",
        "pragma": "no-cache",
        "referer": "https://news.sina.com.cn/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.post(url=url, headers=headers, data=params)
    print(res.text)

login()
