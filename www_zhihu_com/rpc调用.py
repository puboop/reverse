# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-05-14
# @Author  : white
# @FileName: rpc调用.py
# @Software: PyCharm
# **************************************
import requests
from urllib.parse import quote
import hashlib

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": "2.0_"
}
cookies ={"自行补充cookie"}

def des_data(arg1):
    data = {"group": "white",
            "action": "file",
            "data1": arg1}
    res = requests.post("http://127.0.0.1:5620/business-demo/invoke", data=data, verify=False).json()
    return res['sign']

def get_md5(S):
    md5 = hashlib.md5()
    md5.update(S.encode('utf-8'))
    return md5.hexdigest()

def get_data(key, next=False):  # 如果想要一页的话，就是False，如果要很多页的时候，传入True
    '''获取搜索的文章信息'''
    # url = "https://www.zhihu.com/api/v4/search_v3"
    q = key
    q = quote(q)
    url = f"https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q={q}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal"
    s = f'101_3_3.0+{url.replace("https://www.zhihu.com", "")}+' + cookies["d_c0"]
    w_st = des_data(get_md5(s))
    headers["x-zse-96"] += w_st
    print(w_st)
    res = requests.get(url=url, headers=headers, cookies=cookies).json()  # json格式，字典格式
    print(res)
get_data("python")
