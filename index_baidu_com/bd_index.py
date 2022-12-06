# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-05
# @Author  : white
# @FileName: bd_index.py
# @Software: PyCharm
# **************************************
import re
import execjs
import time
import requests

query = "php"

def get_t_key_iv():
    url = "https://dlswbr.baidu.com/heicha/mm/2057/acs-2057.js"
    headers = {
        "referer": "https://index.baidu.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers).text
    info = {
        "text": {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "url": f"https://index.baidu.com/v2/main/index.html#/trend/{query}?words={query}",
            "platform": "Win32",
            "clientTs": int(time.time() * 1000),
            "version": "1.0.0.5"}
    }
    result = re.findall("(var a=function\(c,d\).*?\);)\(", res, re.DOTALL)[0] + "function white(){return a};"
    c = execjs.compile(result).call("white")
    for i, n in enumerate(c):
        r = re.search('\d{13}_', n)
        if r:
            info["timeStamp"] = r.group()
            i += 2
            info["key"] = c[i]
            i += 1
            info["iv"] = c[i]
    return info


def get_data():
    info = get_t_key_iv()
    # 测试用例
    # info = {
    #     'text': {
    #         "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    #         "url": "https://index.baidu.com/v2/main/index.html#/trend/php?words=php",
    #         "platform": "Win32",
    #         "clientTs": 1670248055892,
    #         "version": "1.0.0.5"
    #     }, 'timeStamp': '1670223943370_', 'key': 'guusaiaaqkqqaawu', 'iv': '1234567887654321'
    # }
    cipher = execjs.compile(open("Cipher-Text.js", encoding="utf-8").read()).call("white_encrypt", info)
    print("加密结果：", cipher)
get_data()
