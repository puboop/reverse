# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-02-03
# @Author  : white
# @FileName: demo.py
# @Software: PyCharm
# **************************************
import base64
import requests
import time
import hashlib

name = "13245678900"
password = "123456"

def get_encode(s):
    n = hashlib.md5(s.encode('utf-8')).hexdigest()
    r = base64.b64encode(s.encode()).decode()
    return base64.b64encode((n[0:8] + r + n[10:14]).encode()).decode()

url = "https://my.leju.com/Settings/Findpwd/checkPwd"
params = {
    "oldPwd": get_encode(name) ,
    "mobile": get_encode(password),
    "noCache": str(int(time.time()*1000))
}
print(params)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "LEJUGLOBAL=fa9bec6d9d1abd32943ecea8c4414ed8; BI_STEP=1; BI_INSIDE={}; BI_INSIDE_VP=; BI_OUTSIDE={}; BI_OUTSIDE_VP=; imclientToken=1414265651_0_6bdf75235934fe5b2b5610576ea84fec_6e5d02a5c4c9ccf3b4856f2356b7711d_; imid=1414265651; relationCache_1414265651=%7B%7D; M_CITY=bj; gatheruuid=63dcfae300c81295; PHPSESSID=clreo25tnj1cqa3rssga1hd181; _third_origin_url=https%3A%2F%2Fesf.leju.com%2Fnn%2F",
    "Host": "my.leju.com",
    "HTTP_X_REQUESTED_WITH": "HTTP_X_REQUESTED_WITH",
    "Pragma": "no-cache",
    "Referer": "https://my.leju.com/web/sso/loginView?&fromurl=https%3A%2F%2Fesf.leju.com%2Fnn%2F",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-LJ-Ajax-Request": "AjaxRequest"
}

res = requests.get(url=url,headers=headers, params=params)
print(res.text)

