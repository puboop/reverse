# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-11
# @Author  : white
# @FileName: douban.py
# @Software: PyCharm
# **************************************
import requests
import re
import execjs
import json

def dencrypt_data(data):
    return execjs.compile(open("white.js", encoding="utf-8").read()).call("decrypt", data)


def get_encrypt_data():
    q = "三国演义"
    url = f"https://search.douban.com/book/subject_search?search_text={q}&cat=1001"
    headers = {
        "Host": "search.douban.com",
        "Referer": "https://book.douban.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    return re.findall('window.__DATA__\s=\s"(.*?)"', res.text, re.DOTALL)[0]

def parse_data(data):
    for i in data["payload"]["items"]:
        room = dict()
        room["title"] = i["title"]
        room["url"] = i["url"]
        room["abstract"] = i["abstract"]
        print(room)

def main():
    result = get_encrypt_data()
    result = dencrypt_data(result)
    parse_data(result)

main()
