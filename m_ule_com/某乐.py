# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-03
# @Author  : white
# @FileName: test.py
# @Software: PyCharm
# **************************************
import requests
import execjs
import time
import re


def get_file():
    url = "https://static.tongdun.net/v3/fm.js?t=" + str(int(int(time.time() * 1000) / 36e5))
    headers = {
        "referer": "https://m.ule.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    with open("fm_web.js", "w", encoding="utf-8") as f:
        f.write(res.text)

    result = eval(res.text.split(";}});}));}(")[1].replace("));})();", ""))
    for i in result:
        if len(i) == 64 and "ABCDEFGHIJK" not in i:
            return i

def get_data():
    version = get_file()
    print(version)
    url = execjs.compile(open("white.js", encoding="utf-8").read()).call("summary", version)
    print(url)
    headers = {
        # "Cookie": "c=GsQF57cb-1671463252690-4a0e4c98729d41494348064; _fmdata=iDeMjKv/MM9Ki5eHn3wWRECHTmao8RRPBf6ct5gy3NC1AFRSa6zqcywW3HEq6+wD9Idwmq56VPkVT8RiXtgc4g==; _xid=6QpHvnQq56qJT54KUea7LgRr2+wfXN4KDe4l7rTFLa0=",
        "Host": "fp.tongdun.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers).text
    print(res)


get_data()
