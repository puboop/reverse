# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-24
# @Author  : white
# @FileName: search.py
# @Software: PyCharm
# **************************************
import requests
import json
import execjs
from urllib import parse

url = "https://www.toutiao.com/2/article/search_sug/"
params = {
    "keyword": "流浪地球",
    "ps_type": "sug",
    "aid": "4916"
}
params["_signature"] = execjs.compile(open("signature.js", encoding='u8').read()).call("white", url+"?"+parse.urlencode(params))
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.toutiao.com/?wid=1674568381002",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

res = requests.post(url=url, headers=headers, data=params)
print(json.dumps(res.json(), ensure_ascii=False, indent=4))
