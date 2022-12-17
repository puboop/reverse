# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-10
# @Author  : white
# @FileName: 翻译.py
# @Software: PyCharm
# **************************************
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import requests
import time
import hashlib
import execjs

url = "https://dict.youdao.com/webtranslate"

def get_key():
    url = "https://dict.youdao.com/webtranslate/key"
    params = {
        "keyid": "webfanyi-key-getter",
        "sign": hashlib.md5("".encode('utf-8')).hexdigest(),
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": str(int(time.time()*1000)),
        "keyfrom": "fanyi.web"
    }

def get_translate(text):
    timeStamp =  str(int(time.time()*1000))
    url = "https://dict.youdao.com/webtranslate"
    params = {
        "i": text,
        "from": "auto",
        "to": "",
        "domain": "0",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": hashlib.md5(f'client=fanyideskweb&mysticTime={timeStamp}&product=webfanyi&key=fsdsogkndfokasodnaso'.encode('utf-8')).hexdigest(),
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": timeStamp,
        "keyfrom": "fanyi.web"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-2017525833@10.112.57.87; OUTFOX_SEARCH_USER_ID_NCOO=1417488388.9777794",
        "Host": "dict.youdao.com",
        "Origin": "https://fanyi.youdao.com",
        "Referer": "https://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.post(url=url, headers=headers, data=params)
    data = execjs.compile(open("decrypt.js", encoding="utf-8").read()).call("decrypt", res.text)
    print(data)
get_translate("绿色")
