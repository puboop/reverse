# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-16
# @Author  : white
# @FileName: login.py
# @Software: PyCharm
# **************************************
import execjs
import requests

url = "http://passport2.chaoxing.com/fanyalogin"
uname = "000000000000"
password = "000000000000"
params = {
    "fid": "-1",
    "uname": execjs.compile(open("white.js", encoding="utf-8").read()).call("white", uname),
    "password": execjs.compile(open("white.js", encoding="utf-8").read()).call("white", password),
    "refer": "http%3A%2F%2Fi.chaoxing.com",
    "t": "true",
    "forbidotherlogin": "0",
    "validate": "",
    "doubleFactorLogin": "0",
    "independentId": "0"
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "193",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "passport2.chaoxing.com",
    "Origin": "http://passport2.chaoxing.com",
    "Pragma": "no-cache",
    "Referer": "http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http://i.chaoxing.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
res = requests.post(url=url, headers=headers, data=params)
print(res.text)
