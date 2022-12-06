# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-06
# @Author  : white
# @FileName: 某球.py
# @Software: PyCharm
# **************************************
import requests
import execjs
import re

cookies = dict()

def get_cookie():
    '''获取acw_tc cookie'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
    }
    url = 'https://xueqiu.com/today'
    res = requests.get(url=url, headers=headers)
    arg1 = re.findall("var\sarg1='(.*)'", res.text)[0]
    cookies.update(res.cookies.get_dict())
    cookies['acw_sc__v2'] = execjs.compile(open('./acw_sc__v2.js', encoding='utf-8').read()).call('white', arg1)
    # 第二次获取cookie
    res = requests.get(url=url, headers=headers, cookies=cookies)
    cookies.update(res.cookies.get_dict())


def get_data():
    if not cookies:
        get_cookie()
    url = 'https://xueqiu.com/statuses/hot/listV2.json'
    data = {
        "since_id": "-1",
        "max_id": "-1",     # 响应头中的 next_id
        "size": "15"
    }
    headers = {
        "Host": "xueqiu.com",
        "Referer": "https://xueqiu.com/today",
        "sec-ch-ua": "\"Chromium\";v=\"106\", \"Microsoft Edge\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
    }
    res = requests.get(url=url, params=data, headers=headers, cookies=cookies).json()
    print('next_id: ',res['next_id'])
    print('next_max_id',res['next_max_id'])
    for i in res['items']:
        room = dict()
        room['标题'] = i['original_status']['title']
        room['描述'] = i['original_status']['description']
        room['原标题'] = i['original_status']['rawTitle']
        room['时间'] = i['original_status']['timeBefore']
        room['标签'] = i['original_status']['tagsForWeb']
        print(room)

get_data()
