# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-05-06
# @Author  : white
# @FileName: spider.py
# @Software: PyCharm
# **************************************
import requests
import re
import json
from lxml import etree
from bs4 import BeautifulSoup
from urllib.parse import urljoin
headers = {
    "Cookie": "",
    "Host": "weixin.sogou.com",
    "Referer": "https://weixin.sogou.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

def get_data():
    url = "https://weixin.sogou.com/weixin"
    params = {
        "ie": "utf8",
        "s_from": "input",
        "_sug_": "y",
        "_sug_type_": "",
        "type": "2",
        "page": "2",
        "query": "pycharm"
    }
    for page in range(1,11):
        params["page"] = str(page)
        res = requests.get(url=url, headers=headers, params=params)
        parse(res.text)
    # with open("data/a.html", "w", encoding="utf-8") as f, open("data/b.png", "wb") as ff:
    #     f.write(res.text)
    #     ff.write(res.content)

def parse(html):
    html = etree.HTML(html)
    lis = html.xpath('.//ul[@class="news-list"]/li')
    for house in lis:
        print(house.xpath('string(.//h3)').strip().replace(" ", ""))
        article_url = house.xpath('.//h3/a/@href')[0].strip()
        article_url = urljoin(base_url, article_url)
        print(article_url)
    print()


if __name__ == '__main__':
    base_url = "https://weixin.sogou.com"
    get_data()
