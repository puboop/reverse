# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-07
# @Author  : white
# @FileName: 同花顺.py
# @Software: PyCharm
# **************************************
import requests
import execjs
from lxml import etree

# 获取hexin-v
def get_hexin_v():
    hexin_v = execjs.compile(open('./hexin_v.js', encoding='utf-8').read()).call('white')
    headers = {
        "Cookie": "v={}".format(hexin_v),
        "hexin-v": hexin_v,
        "Host": "q.10jqka.com.cn",
        "Referer": "http://q.10jqka.com.cn/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    }
    return headers

# 获取网页数据
def get_page():
    headers = get_hexin_v()
    for num in range(1,5):
        url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{num}/ajax/1/'.format(num=num)
        yield requests.get(url=url, headers=headers).text

# 获取数据
map = lambda x: x[0] if x else '无'


#解析网页数据
def parse_page():
    numbers = 0
    for page in get_page():
        html = etree.HTML(page)
        tbody = html.xpath('.//tbody/tr')
        for room in tbody:
            numbers += 1
            goods = dict()
            code = map(room.xpath('.//td[2]//text()'))
            name = map(room.xpath('.//td[3]//text()'))
            price = map(room.xpath('.//td[4]//text()'))
            Turnover = map(room.xpath('.//td[11]//text()'))
            Tradable = map(room.xpath('.//td[12]//text()'))
            goods['代码'] = code
            goods['名称'] = name
            goods['现价'] = price
            goods['成交额'] = Turnover
            goods['流通股'] = Tradable
            print(goods)
    print('共计：{}支股票'.format(numbers))

if __name__ == '__main__':
    parse_page()
