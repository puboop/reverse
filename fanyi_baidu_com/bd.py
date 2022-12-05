# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-5
# @Author  : 微信公众号：小白逆向
# @FileName: bd.py
# @Software: PyCharm
# ==================================
import requests
import execjs
import re
query = "小白逆向"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://fanyi.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
}
cookies = dict()
match_k_v = dict()
EXC = execjs.compile(open('make.js', encoding='utf-8').read())

def match_data():
    '''将请求所携带的数据一次性实现'''
    headers = {
        "referer": "https://fanyi.baidu.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = 'https://fanyi.baidu.com/'
    # cookie获取
    cookies.update(requests.get(url, headers).cookies.get_dict())
    res = requests.get(url, headers, cookies=cookies)
    # 获取token
    match_k_v["token"] = re.search("token: '([0-9a-z]+)'", res.text, re.DOTALL).group(1)
    # 获取 gtk
    match_k_v["window_gtk"] = re.findall('window.gtk\s=\s"(\d+.\d+)";', res.text, re.DOTALL)[0]
    url = 'https://dlswbr.baidu.com/heicha/mm/2060/acs-2060.js'
    # 获取时间戳，key，iv
    res = requests.get(url, headers, cookies=cookies)
    encrypt = re.findall("\w{10,16}", re.findall('p.run\(\[(.*?)\]\)', res.text, re.DOTALL)[0])
    match_k_v['timeStamp'] = encrypt[0]

def get_make():
    sign = EXC.call('white_sign', query, match_k_v["window_gtk"])
    headers['Acs-Token'] = EXC.call('white_encrypt', query, headers["User-Agent"], match_k_v["timeStamp"])
    return {
        "from": "zh",
        "to": "en",
        "query": query,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": match_k_v["token"],
        "domain": "common"
    }

def get_result():
    url = 'https://fanyi.baidu.com/v2transapi'
    load = {
        "from": "zh",
        "to": "en"
    }
    data = get_make()
    print(headers["Acs-Token"])
    res = requests.post(url=url, params=load, headers=headers, cookies=cookies, data=data).json()
    if len(res['trans_result']['data']) == 1:
        print(res['trans_result']['data'][0]['dst'])
        return
    words = ""
    for i in res['trans_result']['data']:
        words += i['dst'] + "\n"
    print(words)

def run():
    match_data()
    get_result()
    
if __name__ == '__main__':
    run()
